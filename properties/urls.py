from django.urls import path

from . import views

urlpatterns = [
    path("", views.property_list, name="property_list"),
    path("<int:pk>/", views.property_detail, name="property_detail"),
    path(
        "create/select-type/",
        views.property_create_select_type,
        name="property_create_select_type",
    ),
    path("create/land/", views.property_create_land, name="property_create_land"),
    path(
        "create/building/",
        views.property_create_building,
        name="property_create_building",
    ),
    path("create/cond/", views.property_create_cond, name="property_create_cond"),
    path("<int:pk>/edit/", views.property_edit, name="property_edit"),
    path("<int:pk>/delete/", views.property_delete, name="property_delete"),
]
