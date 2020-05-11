from django.conf.urls import url

from .views import ImageView

image_list = ImageView.as_view({
    'get': 'list',
    'post': 'create'
})
image_detail = ImageView.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = (
    url(r'^$', image_list, name='image-list'),
    url(r'^(?P<pk>[0-9]+)$', image_detail, name='image-detail'),
)
