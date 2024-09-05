from django.urls import path
from .views import IssueListView, IssueDetailView, IssueCreateView

urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('new/', IssueCreateView.as_view(), name='issue_create'),
]