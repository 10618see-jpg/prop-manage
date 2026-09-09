from django.urls import path

from . import views

urlpatterns = [
    path("", views.inquiry_list, name="inquiry_list"),
    path("<int:pk>/", views.inquiry_detail, name="inquiry_detail"),
    path("create/", views.inquiry_create, name="inquiry_create"),
    path("<int:pk>/edit/", views.inquiry_edit, name="inquiry_edit"),
    path("<int:pk>/delete/", views.inquiry_delete, name="inquiry_delete"),
]
