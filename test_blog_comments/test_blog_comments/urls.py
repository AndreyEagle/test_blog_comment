from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1',
        description='Документация',
    ),
    patterns=[path('api/', include('api.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url('swagger-ui/', TemplateView.as_view(
        template_name='swaggerui.html',
        extra_context={'schema_url': 'openapi-schema'}),
        name='swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns = (
        urlpatterns
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
