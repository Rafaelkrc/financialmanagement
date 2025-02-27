def add_bank_balance_on_debit(bank_account, debit_value):
    """
    Atualiza o saldo do banco após um lançamento de débito.
    """
    bank_account.current_balance += debit_value
    bank_account.save(update_fields=['current_balance'], update_from_posting=True)


def add_bank_balance_on_credit(bank_account, credit_value):
    """
    Atualiza o saldo do banco após um lançamento de crédito.
    """
    bank_account.current_balance += credit_value
    bank_account.save(update_fields=['current_balance'], update_from_posting=True)


def update_bank_balance(bank_account, debit_value):
    """
    Atualiza o saldo do banco após uma alteração de lançamento de débitoou crédito.
    """
    bank_account.current_balance -= debit_value
    bank_account.save(update_fields=['current_balance'], update_from_posting=True)
