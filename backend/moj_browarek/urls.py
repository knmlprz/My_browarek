from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

# imports
from user.views import UserViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"profiles", UserProfileViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api_schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api_show/", SpectacularSwaggerView.as_view(url_name="schema")),
]
