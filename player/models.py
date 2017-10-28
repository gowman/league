# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
