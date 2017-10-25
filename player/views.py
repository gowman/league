# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def player_list(arg):
    print arg
    return JsonResponse({'resp': 'arg'})
