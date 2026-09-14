from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import UserRole
from core.decorators import role_required

from .forms import CustomerCreateForm
from .models import Customer


# Create your views here.
# 「管理者/スタッフ/閲覧専用」に対応するリスト
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR, UserRole.VIEWER])
# Customerモデルから全件を取得する
def customer_list(request):
    customers = Customer.objects.all()
    # 取得したデータをテンプレートに渡して表示する
    return render(request, "customers/customer_list.html", {"customers": customers})


# customer_detail
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR, UserRole.VIEWER])
# Customerモデルから指定されたIDの顧客情報を取得する
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    # 取得したデータをテンプレートに渡して表示する
    return render(request, "customers/customer_detail.html", {"customer": customer})


# customer_create
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR])
def customer_create(request):
    if request.method == "POST":
        form = CustomerCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_list")
    else:
        form = CustomerCreateForm()
    return render(request, "customers/customer_create.html", {"form": form})


# customer_update
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR])
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerCreateForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_list")
    else:
        form = CustomerCreateForm(instance=customer)
    return render(request, "customers/customer_form.html", {"form": form})


# customer_delete
@login_required
@role_required([UserRole.ADMIN])
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")
    return render(request, "customers/customer_confirm_delete.html", {"customer": customer})
