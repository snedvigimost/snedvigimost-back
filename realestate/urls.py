from realestate.taggs.views import TagsView
from realestate.comments.views import CommentView
import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .apartment_condition.views import ApartmentConditionView
from .bathroom_type.views import BathroomTypeView
from .heating_type.views import HeatingTypeView
from .images.views import ImageView
from .news.views import NewsView
from .users.views import UserViewSet, UserCreateViewSet
from .listings.views import ListingViewSet, ListingsSelectsView
from .house_types.views import HouseTypeView
from .countries.views import CountryView
from .districts.views import DistrictsView
from .streets.views import StreetsView
from .micro_districts.views import MicroDistrictsView
from .layout.views import LayoutsView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'house-types', HouseTypeView)
router.register(r'listings', ListingViewSet)
router.register(r'countries', CountryView)
router.register(r'districts', DistrictsView)
router.register(r'streets', StreetsView)
router.register(r'micro-districts', MicroDistrictsView)
router.register(r'apartment-condition', ApartmentConditionView)
router.register(r'bathroom-type', BathroomTypeView)
router.register(r'layouts', LayoutsView)
router.register(r'heating-type', HeatingTypeView)
router.register(r'images', ImageView)
router.register(r'news', NewsView)
router.register(r'comments', CommentView)
router.register(r'tags', TagsView)
router.register(r'lising-properties', ListingsSelectsView, basename='LisingProperties')

urlpatterns = [
                  url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                      name='schema-json'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  path('admin/', admin.site.urls),
                  path('__debug__/', include(debug_toolbar.urls)),
                  path('api/', include(router.urls)),
                  path('api-token-auth/', views.obtain_auth_token),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                  # the 'api-root' from django rest-frameworks default router
                  # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
                  re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
