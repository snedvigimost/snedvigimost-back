from realestate.taggs.serializers import TagSerializer
from realestate.taggs.models import Tag
from rest_framework import viewsets

from realestate.users.permissions import IsUserOrReadOnly


class TagsView(viewsets.ModelViewSet):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsUserOrReadOnly,)
