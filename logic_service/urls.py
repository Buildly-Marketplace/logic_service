from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from logic.views import RestaurantViewSet, MenuViewSet
from .views import health_check

router = routers.SimpleRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Logic Service API",
        default_version='latest',
        description="A Buildly RAD Core Compatible Logic Module/microservice.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^docs/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('health_check/', view=health_check, name='health_check'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = urlpatterns + debug_toolbar_urls()