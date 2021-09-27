from django.urls import path


from . import views

urlpatterns = [
    path('add_expense', views.ADDExpense.as_view()),
]