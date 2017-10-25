# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from player.models import Player

class Score(models.Model):
    game = models.DateTimeField()
    home = models.ForeignKey('player.Player', related_name='home')
    away = models.ForeignKey('player.Player', related_name='away')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
