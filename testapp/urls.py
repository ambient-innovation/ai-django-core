from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from testapp.api.urls import model_router

router = routers.DefaultRouter()
router.registry.extend(model_router.registry)

urlpatterns = [
    # django Admin
    path('admin/', admin.site.urls),

    # REST Viewsets
    path('api/v1/', include(router.urls)),
]
