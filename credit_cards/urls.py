from django.urls import path
from . import views

urlpatterns = [
    path('credit_card/list/', views.CreditCardListView.as_view(), name='credit_card_list'),
    path('credit_card/create/', views.CreditCardCreateView.as_view(), name='credit_card_create'),
    path('credit_card/<int:pk>/detail/', views.CreditCardDetailView.as_view(), name='credit_card_detail'),
    path('credit_card/<int:pk>/update/', views.CreditCardUpdateView.as_view(), name='credit_card_update'),
    path('credit_card/<int:pk>/delete/', views.CreditCardDeleteView.as_view(), name='credit_card_delete'),
]
