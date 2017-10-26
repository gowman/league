from rest_framework.viewsets import ModelViewSet
from .serializers import ScoreSerializer
from .models import Score
 
class ScoreViewSet(ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
