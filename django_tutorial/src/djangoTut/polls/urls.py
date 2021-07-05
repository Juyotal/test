from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('bonus/', views.BonusView.as_view(), name='bonus'),
    path('create-question/',views.QuestionCreate.as_view(), name = 'questioncreate'),
    path('<int:pk>/delete-question/',views.QuestionDelete.as_view(), name = 'questiondel'),
    path('<int:pk>/add-choice/',views.AddChoice.as_view(), name = 'choiceadd'),
    path('login/', views.CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'polls:index'), name = 'logout'),
]