from django.contrib import admin
from .models import Team, Player, Season, TeamSeason, Game, Goal, PlayerGame

admin.site.register(Team)
admin.site.register(Season)
admin.site.register(TeamSeason)
admin.site.register(Game)
admin.site.register(Goal)
admin.site.register(PlayerGame)