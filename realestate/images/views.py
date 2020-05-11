from rest_framework import viewsets

from realestate.images.models import Image
from realestate.images.serializers import ImageSerializer
from realestate.users.permissions import IsUserOrReadOnly


class ImageView(viewsets.ModelViewSet):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsUserOrReadOnly,)
