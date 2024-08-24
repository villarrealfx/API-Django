from django.urls import path
from django.contrib import admin
from core import views as core_views
from ecommerce import views as ecommerce_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'item', ecommerce_views.ItemViewSet, basename='item')
router.register(r'order', ecommerce_views.OrderViewSet, basename='order')

schema_view = get_schema_view(
   openapi.Info(
      title="Django_API docs",
      default_version='v1',
      description="Test description",
      terms_of_service=" ",
      contact=openapi.Contact(email="villarreal.fx@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
