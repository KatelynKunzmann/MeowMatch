from django.urls import re_path, include
from CatApp import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^cat$',views.catApi),
    re_path(r'^cat/([0-9]+)$',views.catApi),

    re_path(r'^employee$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),
#possible delete of /([0-9]+)$/ if doesnt work
    re_path(r'^employee/([0-9]+)$/savefile',views.SaveFile),
    re_path(r'^cat/([0-9]+)$/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)