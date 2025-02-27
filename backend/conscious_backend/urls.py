"""
URL configuration for conscious_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from conscious_backend import views

schema_view = get_schema_view(
    openapi.Info(
        title="Co2-nscious",
        default_version="v1",
        description="Co2-nscious Website API description",
        contact=openapi.Contact(email="ranoprog@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api-auth/", include("rest_framework.urls")),
    # path('api/auth/registration/', include('dj_rest_auth.registration.urls')),


    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path('', views.index, name='index'),
    path('measures/', include('co2measures.urls')), # Required for REST apis using ListCreateAPIView 
    path('action/', include('action.urls')),
    path('employeeprofile/', include('employeeprofile.urls')),
    path('badge/', include('badge.urls')),
    path('category/', include('category.urls')),
    path('motivation/', include('motivation.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
