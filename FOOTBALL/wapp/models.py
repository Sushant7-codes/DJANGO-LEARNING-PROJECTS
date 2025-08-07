from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=100)
    founded_date = models.DateField()
    stadium = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Player(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    birth_date = models.DateField()
    def __str__(self):
        return self.name
    
class Match(models.Model):
    home_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='home_matches')
    away_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='away_matches')
    match_date = models.DateField()
    stadium = models.CharField(max_length=100)
    referee = models.CharField(max_length=100)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    match_result = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.home_club} vs {self.away_club}"
    
    class Meta:
        verbose_name_plural = 'Matches'
    
class MatchEvent(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    minute = models.IntegerField()
    event_type = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.player.name} - {self.event_type}"
    
class PlayerProfile(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='player_images/', null=True, blank=True)
    def __str__(self):
        return f"{self.player.name}'s Profile"