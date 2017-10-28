from rest_framework.viewsets import ModelViewSet

from .models import Team
from .serializers import TeamSerializer


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
