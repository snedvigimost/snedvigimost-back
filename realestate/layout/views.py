# Create your views here.
from rest_framework import viewsets

from realestate.layout.models import Layout
from realestate.layout.serializers import LayoutSerializer
from realestate.users.permissions import IsUserOrReadOnly


class LayoutsView(viewsets.ModelViewSet):
    model = Layout
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer
    permission_classes = (IsUserOrReadOnly,)
