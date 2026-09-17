# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import UserRole
from core.decorators import role_required

from .forms import BuildingForm, CondForm, LandForm
from .models import Property, PropertyType


# 	種別選択画面の作成
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR])
def property_create_select_type(request):
    return render(request, "properties/property_create_select_type.html")


# 	土地作成画面の作成
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR])
def property_create_land(request):
    if request.method == "POST":
        form = LandForm(request.POST)
        if form.is_valid():
            # データベースへの保存を一時保留し、オブジェクトだけ取得する
            land = form.save(commit=False)
            # property_typeのセット
            land.property_type = PropertyType.LAND
            land.save()
            return redirect("property_list")
    else:
        form = LandForm()
    return render(request, "properties/property_create_land.html", {"form": form})


# 	建物作成画面の作成
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR])
def property_create_building(request):
    if request.method == "POST":
        form = BuildingForm(request.POST)
        if form.is_valid():
            building = form.save(commit=False)
            building.property_type = PropertyType.BUILDING
            building.save()
            return redirect("property_list")
    else:
        form = BuildingForm()
    return render(request, "properties/property_create_building.html", {"form": form})


# 	Cond作成画面の作成
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR])
def property_create_cond(request):
    if request.method == "POST":
        form = CondForm(request.POST)
        if form.is_valid():
            condo = form.save(commit=False)
            condo.property_type = PropertyType.COND
            condo.save()
            return redirect("property_list")
    else:
        form = CondForm()
    return render(request, "properties/property_create_cond.html", {"form": form})


# 	物件一覧画面の作成
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR, UserRole.VIEWER])
def property_list(request):
    properties = Property.objects.all()
    return render(request, "properties/property_list.html", {"properties": properties})
