from rest_framework import serializers
from .models import Team, TeamSeason, Season, Player

class TeamSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSeason
        fields = ['id', 'wins', 'losses', 'ties', 'season']

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['name']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name']
    
class TeamSerializer(serializers.ModelSerializer):
    teamseason_team_requests_created = TeamSeasonSerializer(many=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'teamseason_team_requests_created']

