from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    address = models.CharField(max_length=254)
    phone = models.CharField(max_length=10)

    def __str___(self):
        return f'{self.first_name} {self.last_name}'

class Season(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class TeamSeason(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teamseason_team_requests_created')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    players = models.ManyToManyField(Player)

    def __str__(self):
        return f'{self.team.name} - {self.season.name}'

class Game(models.Model):
    game_date = models.DateField()
    team_home = models.ForeignKey(TeamSeason, on_delete=models.CASCADE, related_name='team_home_requests_created')
    team_away = models.ForeignKey(TeamSeason, on_delete=models.CASCADE, related_name='team_away_requests_created')

    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    home_shots = models.IntegerField()
    away_shots = models.IntegerField()

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

class PlayerGame(models.Model) :
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='playergame_game_requests_created')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='playergame_player_requests_created')

    shots = models.IntegerField()