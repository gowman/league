from rest_framework.viewsets import ModelViewSet

from player.models import Player
from player.serializers import PlayerSerializer


class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
