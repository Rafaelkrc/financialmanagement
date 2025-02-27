from django.db import models, transaction
from django.utils import timezone
from categories.models import Category, SubCategory
from bank_account.models import BankAccount
from account_postings.metrics import add_bank_balance_on_debit, add_bank_balance_on_credit, update_bank_balance


class AccountPosting(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    issue_date = models.DateField()
    description = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='account_posting_category')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='account_posting_category')
    bank = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name='account_posting_bank_account')
    expiry_date = models.DateField()
    debit_value = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    credit_value = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    transfer_pair = models.OneToOneField(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="paired_transfer"
    )
    transfering = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Verifica se o lançamento já existe no banco de dados
        if self.pk:
            original = AccountPosting.objects.get(pk=self.pk)

            # Se houver uma alteração no débito, reverte o impacto do lançamento original
            if original.debit_value != self.debit_value:
                update_bank_balance(self.bank, original.debit_value)

            # Se houver uma alteração no crédito, reverte o impacto do lançamento original
            if original.credit_value != self.credit_value:
                update_bank_balance(self.bank, original.credit_value)

        self.credit_value = abs(self.credit_value)  # Garante que o valor seja positivo
        if self.debit_value > 0:
            self.debit_value = -abs(self.debit_value)  # Garante que o valor seja negativo

        super().save(*args, **kwargs)

        # Atualiza apenas os campos do par, sem chamar save() diretamente
        if self.transfer_pair:
            AccountPosting.objects.filter(pk=self.transfer_pair.pk).update(
                debit_value=-self.credit_value,
                credit_value=-self.debit_value
            )

        # Atualiza o saldo com os novos valores
        if not self.transfering:
            if self.debit_value != 0:
                add_bank_balance_on_debit(self.bank, self.debit_value)
            elif self.credit_value != 0:
                add_bank_balance_on_credit(self.bank, self.credit_value)

    @classmethod
    def transfer(cls, from_bank, to_bank, value, description, issue_date, expiry_date, category, subcategory):
        if from_bank == to_bank:
            raise ValueError("A conta de origem e destino não podem ser a mesma.")

        if value <= 0:
            raise ValueError("O valor da transferência deve ser maior que zero.")

        with transaction.atomic():  # Gera os dois lançamentos simultaneos

            category, _ = Category.objects.get_or_create(name="Transferência")
            subcategory, _ = SubCategory.objects.get_or_create(name="Transferência")
            # Criar o lançamento de débito
            debit_posting = cls.objects.create(
                bank=from_bank,
                debit_value=-abs(value),
                credit_value=0,
                description=f"Transferência para {to_bank.name}: {description}",
                issue_date=timezone.now(),
                expiry_date=timezone.now(),
                category=Category.objects.get(name="Transferência"),
                subcategory=SubCategory.objects.get(name="Transferência"),
                transfering=True,
            )

            # Criar o lançamento de crédito
            credit_posting = cls.objects.create(
                bank=to_bank,
                debit_value=0,
                credit_value=abs(value),
                description=f"Transferência de {from_bank.name}: {description}",
                issue_date=timezone.now(),
                expiry_date=timezone.now(),
                category=Category.objects.get(name="Transferência"),
                subcategory=SubCategory.objects.get(name="Transferência"),
                transfering=True,
            )

            # Atualizar os dois objetos para criar o vínculo
            debit_posting.transfer_pair = credit_posting
            credit_posting.transfer_pair = debit_posting
            # Apenas atualizamos os campos necessários, sem chamar `save()` novamente
            AccountPosting.objects.filter(pk=debit_posting.pk).update(transfer_pair=credit_posting)
            AccountPosting.objects.filter(pk=credit_posting.pk).update(transfer_pair=debit_posting)

            # Atualiza saldos das contas
            if debit_posting.transfering and credit_posting.transfering:
                add_bank_balance_on_debit(from_bank, -abs(value))
                add_bank_balance_on_credit(to_bank, abs(value))

        return debit_posting, credit_posting

    def delete(self, *args, **kwargs):
        # Reverte o impacto do lançamento no saldo da conta bancária antes de deletá-lo
        if self.debit_value != 0:
            update_bank_balance(self.bank, self.debit_value)  # Reverte o débito
        elif self.credit_value != 0:
            update_bank_balance(self.bank, self.credit_value)  # Reverte o crédito

        if self.transfer_pair:
            # Salva a referência antes de excluir o primeiro objeto
            pair = self.transfer_pair
            self.transfer_pair = None
            self.save(update_fields=['transfer_pair'])  # Remove a referência antes da exclusão

            # Exclui o lançamento vinculado
            pair.transfer_pair = None  # Remove a referência do outro lançamento
            pair.delete()

        super().delete(*args, **kwargs)  # Deleta o lançamento

    def category_name(self):
        return self.category.name
    category_name.name = 'Category'

    def subcategory_name(self):
        return self.subcategory.name
    subcategory_name.name = 'SubCategory'

    def bank_name(self):
        return self.bank.name
    bank_name.name = 'Bank'
