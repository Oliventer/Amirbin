from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from notepad import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
