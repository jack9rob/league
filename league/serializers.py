from rest_framework import serializers
from .models import Team, TeamSeason, Season, Goal
from users.models import Player
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class PlayerSerializer(serializers.ModelSerializer):
    # Create a custom method field
    user = UserSerializer()

    class Meta:
        model = Player
        fields = ['address', 'user']

class TeamSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSeason
        fields = ['id', 'wins', 'losses', 'ties', 'season']


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['name']
 
class TeamSerializer(serializers.ModelSerializer):
    teamseason_team_requests_created = TeamSeasonSerializer(many=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'teamseason_team_requests_created']

class TeamSeasonSerializerDetail(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(read_only=True, slug_field='name')
    players = PlayerSerializer(many=True)
    season = SeasonSerializer()
    class Meta:
        model = TeamSeason
        fields = ['id', 'wins', 'losses', 'ties', 'season', 'players', 'team']
    
class GoalSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    primary_assist = PlayerSerializer()
    secondary_assist = PlayerSerializer()
    class Meta:
        model = Goal
        fields = ['id', 'player', 'primary_assist', 'secondary_assist']