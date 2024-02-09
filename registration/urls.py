"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from register.views import register
from dashboard.views import dashboard
from dashboard.views import leistungserbringerDatenAenderung

from pdfVerarbeitung.views import unterschriftView
from pdfVerarbeitung.views import unterschriftsBestaetigungView


urlpatterns = [
    #authentification
    path("accounts/", include("django.contrib.auth.urls")),

    path('admin/', admin.site.urls),
    path("register/", register),
    path("register/<str:kundenDaten>", register),
    path("dashboard/", dashboard),
    path("unterschrift/", unterschriftView),
    path("unterschrift/<str:unterschriftsDaten>", unterschriftView),

    # Ajax Requests
    path("unterschriftsbestaetigung", unterschriftsBestaetigungView, name="unterschriftsbestaetigung"),
    path("leistungserbringerdatenaenderung", leistungserbringerDatenAenderung, name="leistungserbringerdatenaenderung"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
