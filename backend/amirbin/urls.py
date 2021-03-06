"""amirbin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notepad.views import NoteViewSet
from users.views import UserViewset
from tokens.views import PasswordlessLoginView, CheckPaswordlessTokenView, PaswordlessTokenViewSet, PaswordlessRegistrationView
from subscriptions.views import CheckoutSessionCreationView, StripeKeyView, StripeWebhook

router = DefaultRouter()
router.register('notes', NoteViewSet)
router.register('users', UserViewset)
router.register('paswordlessTokens', PaswordlessTokenViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('token/login/<str:user_email>/', PasswordlessLoginView.as_view()),
    path('token/auth/<str:user_email>/', PaswordlessRegistrationView.as_view()),
    path('token/check/<str:token_id>/', CheckPaswordlessTokenView.as_view()),
    path('subscribe/key/', StripeKeyView.as_view()),
    path('subscribe/<str:product_name>/', CheckoutSessionCreationView.as_view()),
    path('stripe/webhook/', StripeWebhook.as_view()),
    ]
