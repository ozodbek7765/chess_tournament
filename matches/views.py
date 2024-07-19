from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Match
from .serializers import MatchSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]
