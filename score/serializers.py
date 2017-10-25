from rest_framework import serializers

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'game', 'home', 'home_score', 'away', 'away_score')
