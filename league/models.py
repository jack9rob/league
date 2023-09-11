from django.db import models
from users.models import Player

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class TeamSeason(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamseason_team_requests_created')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    players = models.ManyToManyField(Player, blank=True)

    def __str__(self):
        return f'{self.team.name} - {self.season.name}'

class Game(models.Model):
    game_date = models.DateTimeField()
    team_home = models.ForeignKey(TeamSeason, on_delete=models.CASCADE, related_name='team_home_requests_created')
    team_away = models.ForeignKey(TeamSeason, on_delete=models.CASCADE, related_name='team_away_requests_created')

    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    home_shots = models.IntegerField()
    away_shots = models.IntegerField()

    def __str__(self):
        return f'{self.team_home.team.name} vs {self.team_away.team.name} at {self.game_date.strftime("%H:%M %b %d ")}'

class Goal(models.Model):
    GOAL_TYPES = [
        ("PP", "Power Play"),
        ("SH", "Short handed"),
        ("EN", "Empty Net")
    ]

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='goal_game_requests_created')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goal_player_requests_created')
    primary_assist = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='goal_primary_assist_requests_created')
    secondary_assist = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='secondary_assist_requests_created')
    goal_type = models.CharField(max_length=2, choices=GOAL_TYPES)

    def __str__(self):
        return f'{self.player.user} from {self.primary_assist.user}, {self.secondary_assist.user}'

class PlayerGame(models.Model) :
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='playergame_game_requests_created')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playergame_player_requests_created')

    shots = models.IntegerField()