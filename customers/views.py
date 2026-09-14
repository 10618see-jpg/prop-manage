from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import UserRole
from core.decorators import role_required

from .models import Customer

from django.shortcuts import render, get_object_or_404, redirect


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