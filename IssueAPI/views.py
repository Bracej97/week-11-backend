from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from issueTrackerBackendApp.models import Issue
from .serializers import IssueSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey



# View for listing all issues
@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @permission_classes([HasAPIKey])
def getAllIssues(request):
    issues = Issue.objects.all()
    serializer = IssueSerializer(issues, many=True)
    return Response({
        "status": True,
        "data": serializer.data
        })

# View for getting issue by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @permission_classes([HasAPIKey])
def getIssueById(request, id):
    try:
        issue = Issue.objects.get(id=id)
    except Issue.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)

    serializer = IssueSerializer(issue)
    return Response(serializer.data)

# View for adding a new issue
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @permission_classes([HasAPIKey])
def addIssue(request):
    serializer = IssueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
# @permission_classes([HasAPIKey])
def updateIssue(request, id):
    try:
        issue = Issue.objects.get(id=id)
        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Issue.DoesNotExist:
        return Response({"error": "Issue not found"}, status=404)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
# @permission_classes([HasAPIKey])
def deleteIssue(request, id):
    try:
        issue = Issue.objects.get(id=id)
    except Issue.DoesNotExist:
        return Response({"error": "Issue not found"}, status=404)

    issue.delete()
    return Response({"message": "Issue deleted successfully"})
