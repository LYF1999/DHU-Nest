from rest_framework import routers
from profile.views import ProfileViewSets

router = routers.DefaultRouter()

router.register('users', ProfileViewSets)