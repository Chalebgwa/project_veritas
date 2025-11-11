from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_business_idea, name='create_business_idea'),
    path('plan/<int:pk>/', views.business_plan_detail, name='business_plan_detail'),
    path('ideas/', views.BusinessIdeaListView.as_view(), name='business_idea_list'),
]
