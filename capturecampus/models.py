from ast import Return
from django.db import models

# Create your models here
# Classes for the models used in the game
# Created by Monty Batt Adam Brooks Mobayode Fashanu George Hynes.

class Team(models.Model):
    name= models.CharField(max_length=250)
    score_1= models.IntegerField(default=0)
    def getName(self):
        return self.name.upper()
    
    def __str__(self):
        return self.name
    def getTeamScore(self):
        self.teamScore = sum([p.getScore() for p in self.player_set.all()])
        return self.teamScore
    def getPlayers(self):
        names = []
        for p in self.player_set.all():
             names.append(p.getName() +"-"+ str(p.getScore()))
        return names
    def get_other_teams(self):
        teams = []
        for p in Team.objects.all():
            teams.append(p.getName()+ " - " + str(p.getTeamScore())+ p.getBestPlayer())
        return teams
    def getBestPlayer(self):
        x = 0
        y = "Nobody"
        for p in self.player_set.all():
            if p.getScore() > x:
                x = p.getScore()
                y = p.getName()
        if x == 0:
            return ""
        return " their top player is "+ y + " " + "with a score of " + str(x)
class Player(models.Model):
    team = models.ForeignKey("Team",  on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='Player')
    score = models.IntegerField(default=0)
    def captured_flag(self,x):
        self.score += x
        self.save()
        return None
    def getScore(self):
        return self.score
    def getTeamScore(self):
        return self.team.score_1    
    def getTeamName(self):
        return self.team.name
    def getTeam(self):
        return self.team
    def __str__(self):
        return self.name
    def getName(self):
        return self.name
    def get_flag():
        x = []
        for y in Flag.objects.all():
            x.append(y)
        return x
LOCATIONS = [('INTO','Into'),('FORUM','Forum'),('QUEENS BUILDING','Queens building'),('AMOURY,Amoury'),('EAST PARK','East park'),('BUISNESS SCHOOL','Buisness School'),('ROWE HOUSE','Rowe House'),('SPORT PARK','Sport park'),('WASHINGTON SINGER','Washington Singer')]
class Flag(models.Model):
    score = models.IntegerField(default=1)
    location = models.CharField(max_length=250,default="Forum")
    code = models.CharField(max_length=250)
    def __str__(self):
        return "Flag at "+ self.location +" with  " + str(self.score) + " points"
    def get_score(self):
        return self.score
    def get_code(self):
        return self.code
    def get_location(self):
        return self.location
    def get_coord(self):
        if self.location.lower() == 'into':
            pass
   