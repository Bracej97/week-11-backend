from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages

#from .forms import IssueForm
from .models import Issue

# Create your views here.

def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'tracker/issue_list.html', {'issues':issues})
