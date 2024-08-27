from django.urls import path
from . import views

urlpatterns = [
    path('currency/list/', views.CurrencyListView.as_view(), name='currency_list'),
    path('currency/create/', views.CurrencyCreateView.as_view(), name='currency_create'),
    path('currency/<int:pk>/detail/', views.CurrencyDetailView.as_view(), name='currency_detail'),
    path('currency/<int:pk>/update/', views.CurrencyUpdateView.as_view(), name='currency_update'),
    path('currency/<int:pk>/delete/', views.CurrencyDeleteView.as_view(), name='currency_delete'),
    path('bank_account/list/', views.BankAccountListView.as_view(), name='bank_account_list'),
    path('bank_account/create/', views.BankAccountCreateView.as_view(), name='bank_account_create'),
    path('bank_account/<int:pk>/detail/', views.BankAccountDetailView.as_view(), name='bank_account_detail'),
    path('bank_account/<int:pk>/update/', views.BankAccountUpdateView.as_view(), name='bank_account_update'),
    path('bank_account/<int:pk>/delete/', views.BankAccountDeleteView.as_view(), name='bank_account_delete'),
]
