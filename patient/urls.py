from django.urls import include, path
from rest_framework import routers
from . import views
from django.urls import include, path
from django.conf.urls import include, url



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts',views.PostsViewSet)
router.register(r'details', views.DetailsViewSet)
router.register(r'info',views.InfoViewSet)
router.register(r'prescription', views.PrescriptionsViewSet)
router.register(r'test',views.TestsViewSet)


urlpatterns = [
    path('', include(router.urls)),    
]
