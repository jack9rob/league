from django.http import JsonResponse
from ..models import TeamSeason
from ..serializers import TeamSeasonSerializer, TeamSeasonSerializerDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

