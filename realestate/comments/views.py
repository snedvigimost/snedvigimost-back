from realestate.comments.serializers import CommentSerializer
from realestate.comments.models import Comment
from rest_framework import viewsets

from realestate.users.permissions import IsUserOrReadOnly


class CommentView(viewsets.ModelViewSet):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsUserOrReadOnly,)
