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
def property_list(
    request,
):
    # 	property_typeで絞込
    properties = Property.objects.all()
    property_type = request.GET.get("type")
    if property_type:
        properties = properties.filter(property_type=property_type)
    # 	statusで絞込
    status = request.GET.get("status")
    if status:
        properties = properties.filter(property_status=status)
    # 	価格帯の絞り込み
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    # 	cityの絞り込み
    city = request.GET.get("city")
    if city:
        properties = properties.filter(city__icontains=city)
    # 	townの絞り込み
    town = request.GET.get("town")
    if town:
        properties = properties.filter(town__icontains=town)
    # 	areaの絞り込み
    min_area = request.GET.get("min_area")
    max_area = request.GET.get("max_area")
    # 	土地の場合
    if property_type == PropertyType.LAND:
        if min_area:
            properties = properties.filter(land__area__gte=min_area)
        if max_area:
            properties = properties.filter(land__area__lte=max_area)
    # 	建物の場合
    if property_type == PropertyType.BUILDING:
        if min_area:
            properties = properties.filter(building__area__gte=min_area)
        if max_area:
            properties = properties.filter(building__area__lte=max_area)
    # 	マンションの場合
    if property_type == PropertyType.COND:
        if min_area:
            properties = properties.filter(cond__area__gte=min_area)
        if max_area:
            properties = properties.filter(cond__area__lte=max_area)
        # 	ペット可否の絞り込み
        pet_policy = request.GET.get("pet_policy")
        if pet_policy:
            properties = properties.filter(cond__pet_policy=pet_policy)

    return render(request, "properties/property_list.html", {"properties": properties})
