from django.http import JsonResponse, HttpResponse
from ..models import Team, TeamSeason, Player, Goal
from ..serializers import TeamSerializer, TeamSeasonSerializerDetail, GoalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

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

@api_view(['GET', 'PUT', 'DELETE'])
def teamseason_detail(request, id):
    try:
        teamSeason = TeamSeason.objects.get(pk=id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TeamSeasonSerializerDetail(teamSeason)
        return JsonResponse(serializer.data)

@api_view(['GET'])
def teamseason_stats(request, id):
    teamSeason = {}
    try:
        teamSeason = TeamSeason.objects.get(pk=id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    stats = []
    '''
    goals = Goal.objects.all()
    serializer = GoalSerializer(goals, many=True)
    return JsonResponse({"goals" : serializer.data}, safe=False)
    '''
    goals = []
    for player in teamSeason.players.all():
        try:
            total = Goal.objects.get(id=player.id, game__team_home__pk=4)
            goals.append(total)
        except Exception as error:
            comment = None
            print(error)

    serializer = GoalSerializer(goals, many=True)
    return JsonResponse({"goals" : serializer.data}, safe=False)
    return JsonResponse({})