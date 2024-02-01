from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account.views import confirm_email as allauthemailconfirmation
from django.views.generic import TemplateView, RedirectView

from rest_auth.views import (
    LoginView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('core.urls', namespace='api')),
    path('accounts/', include('allauth.account.urls')),
    path(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    path('login/', LoginView.as_view(), name='rest_login'),
]