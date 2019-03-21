from django.db import models

class Country(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class League(models.Model) :
    name = models.CharField(max_length=128)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class Team(models.Model) :
    name = models.CharField(max_length=128)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE)
    league_id = models.ForeignKey('League', on_delete=models.CASCADE)
    matches = models.ManyToManyField('Team')

    def __str__(self) :
        return self.name

class Match(models.Model) :
    name = models.CharField(max_length=128)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE)
    league_id = models.ForeignKey('League', on_delete=models.CASCADE)
    teams = models.ManyToManyField('Team', on_delete=models.CASCADE)
    players = models.ManyToManyField('Player', on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class Player_Attribute(models.Model):
    jumping = models.FloatField(null=True)
    defensive_work_rate = models.FloatField(null=True)
    attacking_work_rate = models.FloatField(null=True)
    overall_rate = models.FloatField(null=True)

    def __str__(self) :
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=128)
    birth = models.TextField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    attribute_id = models.ForeignKey('Player_Attribute', on_delete=models.CASCADE)
    league_id = models.ForeignKey('League', on_delete=models.CASCADE)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE)
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE)
    matches = models.ManyToManyField('Match', on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
