from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_quiz, name='all_quiz'),
    path('<int:quiz_id>/', views.quiz_view, name='quiz_view'),
]
