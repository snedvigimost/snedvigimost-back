from rest_framework import viewsets, pagination
from rest_framework_extensions.decorators import paginate

from realestate.images.models import Image
from realestate.images.serializers import ImageSerializer
from realestate.users.permissions import IsUserOrReadOnly


@paginate(pagination_class=pagination.PageNumberPagination, page_size=20)
class ImageView(viewsets.ModelViewSet):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsUserOrReadOnly,)
