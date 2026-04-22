from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

from apps.hashtags.urls import hashtag_router


api_router = routers.DefaultRouter()

api_router.registry.extend(
    hashtag_router.registry
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")

]
