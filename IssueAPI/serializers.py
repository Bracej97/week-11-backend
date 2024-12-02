from rest_framework import serializers
from issueTrackerBackendApp.models import Issue

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['issue_name', 'issue_description', 'issue_status', 'date_created']
