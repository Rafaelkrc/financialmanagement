from django.urls import path
from . import views

urlpatterns = [
    path('account_postings/list/', views.AccounPostingListView.as_view(), name='account_postings_list'),
]
