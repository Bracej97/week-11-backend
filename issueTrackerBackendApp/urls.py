from django.urls import path

from issueTrackerBackendApp import views

urlpatterns = [
    path('', views.issue_list, name='issue_list'),
    path('issue/<int:id>/', views.issue_detail, name='issue_detail'),
    path('issue/new/', views.issue_new, name='issue_new'),
    path('issue/<int:id>/edit/', views.issue_edit, name='issue_edit'),
    path('issue/<int:id>/delete', views.issue_delete, name='issue_delete')
]
