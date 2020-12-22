from rest_framework import viewsets

from realestate.news.models import News
from realestate.news.serializers import NewsSerializer
from realestate.users.permissions import IsUserOrReadOnly


class NewsView(viewsets.ModelViewSet):
    model = News
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsUserOrReadOnly,)
