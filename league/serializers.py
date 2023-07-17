from rest_framework import serializers
from .models import Team

class TeamSeraializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']