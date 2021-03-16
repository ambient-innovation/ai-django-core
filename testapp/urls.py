from django.urls import path, include
from rest_framework import routers

from testapp.api.urls import model_router

router = routers.DefaultRouter()
router.registry.extend(model_router.registry)

urlpatterns = [
    # REST Viewsets
    path('api/v1/', include(router.urls)),
]
