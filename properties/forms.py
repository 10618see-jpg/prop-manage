from django import forms

from .models import Building, Cond, Land


# LandFormの作成
class LandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = [
            "area",
            "land_category",
            "building_coverage_ratio",
            "floor_area_ratio",
            "land_right_type",
            "price",
            "city",
            "town",
            "street",
            "latitude",
            "longitude",
            "property_status",
            "manager",
            "seller",
        ]


# BuildingFormの作成
class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            "area",
            "building_structure",
            "building_year",
            "build_month",
            "floor_plan",
            "road_access",
            "price",
            "city",
            "town",
            "street",
            "latitude",
            "longitude",
            "property_status",
            "manager",
            "seller",
        ]


# CondFormの作成
class CondForm(forms.ModelForm):
    class Meta:
        model = Cond
        fields = [
            "area",
            "condominium_name",
            "room_number",
            "floor",
            "management_fee",
            "maintenance_fee",
            "pet_policy",
            "management_type",
            "price",
            "city",
            "town",
            "street",
            "latitude",
            "longitude",
            "property_status",
            "manager",
            "seller",
        ]
