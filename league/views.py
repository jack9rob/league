from django.http import JsonResponse
from .models import Team
from .serializers import TeamSeraializer

def team_list(request):
    teams = Team.objects.all()
    serializer = TeamSeraializer(teams, many=True)
    return JsonResponse({"teams" : serializer.data}, safe=False)
