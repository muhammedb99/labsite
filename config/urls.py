"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from core.views import home, start_view,inputs_view,results_view,results_pdf_view,reference_ranges_view
from django.views.generic import RedirectView
from django.templatetags.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('start/', start_view, name='start'),
    path('inputs/', inputs_view, name='inputs'),
    path('results/', results_view, name='results'),
    path('results.pdf', results_pdf_view, name='results_pdf'),
    path("reference/", reference_ranges_view, name="reference_ranges"),
    path(
            "favicon.ico",
            RedirectView.as_view(url=static("imgs/lab_icon.svg"), permanent=False),
        ),
]
