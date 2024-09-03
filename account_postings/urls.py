from django.urls import path
from . import views

urlpatterns = [
    path('account_postings/list/', views.AccountPostingListView.as_view(), name='account_postings_list'),
    path('account_postings/create/debit/', views.AccountPostingCreateDebitView.as_view(), name='account_postings_create_debit'),
    path('account_postings/create/credit/', views.AccountPostingCreateCreditView.as_view(), name='account_postings_create_credit'),
    path('account_postings/<int:pk>/detail/', views.AccountPostingDetailView.as_view(), name='account_postings_detail'),
    path('account_postings/<int:pk>/update/credit/', views.AccountPostingUpdateCreditView.as_view(), name='account_postings_update_credit'),
    path('account_postings/<int:pk>/update/debit/', views.AccountPostingUpdateDebitView.as_view(), name='account_postings_update_debit'),
    path('account_postings/<int:pk>/delete/', views.AccountPostingDeleteView.as_view(), name='account_postings_delete'),
]
