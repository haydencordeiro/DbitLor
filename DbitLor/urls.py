from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="DBITLOR API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cordeirohayden@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', include('endpointApp.urls')),
    path('admin/', admin.site.urls),
    path('api/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    # path('api-auth/', include('rest_framework.urls'))
    # url(r'^auth/', include('djoser.urls')),
]
