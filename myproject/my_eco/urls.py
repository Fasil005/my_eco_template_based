from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('add_expense', views.ADDExpense.as_view(),name='add_expense'),
    path('add_income', views.ADDIncome.as_view(),name='add_inome'),
    path('add_loan', views.ADDLoan.as_view(),name='add_loan'),
    path('add_balance', views.ADDBalance.as_view(),name='add_balance'),
    path('income', views.income,name='income'),
    url('expense', views.expense,name='expense'),
    url('loan', views.loan,name='loan'),
    url(r'^$', views.index),
]