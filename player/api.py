from rest_framework.viewsets import ModelViewSet
from player.serializers import PlayerSerializer
from player.models import Player
 
class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
