from django.http import JsonResponse
from ..models import Team
from ..serializers import TeamSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def team_list(request):

    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return JsonResponse({"teams" : serializer.data}, safe=False)

    if request.method == 'GET':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, id):
    try:
        team = Team.objects.get(pk=id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TeamSerializer(team)
        return JsonResponse(serializer.data)