from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllIssues),
    path('add/', views.addIssue),
    path('get/<int:id>/', views.getIssueById, name='get_issue_by_id'),
    path('delete/<int:id>/', views.deleteIssue, name='delete_issue'),
    path('update/<int:id>/', views.updateIssue, name='update_issue'),
]
