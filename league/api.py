from rest_framework.routers import DefaultRouter
from player.api import PlayerViewSet
from score.api import ScoreViewSet
 
router = DefaultRouter()
 
router.register('player', PlayerViewSet)
router.register('score', ScoreViewSet)
