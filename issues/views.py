from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Issue

class IssueListView(ListView):
    model = Issue
    template_name = 'issue_list.html'
    context_object_name = 'issues'

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue_detail.html'
    context_object_name = 'issue'

class IssueCreateView(CreateView):
    model = Issue
    template_name = 'issue_form.html'
    fields = ['title', 'description', 'status', 'assigned_to']
    success_url = reverse_lazy('issue_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)