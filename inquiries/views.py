from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import UserRole
from core.decorators import role_required

from .forms import InquiryForm
from .models import Inquiry


# Create your views here.
# inquiriesの一覧
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR, UserRole.VIEWER])
def inquiry_list(request):
    inquiries = Inquiry.objects.all()
    return render(request, "inquiries/inquiry_list.html", {"inquiries": inquiries})


# inquiriesの詳細
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR, UserRole.VIEWER])
def inquiry_detail(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    return render(request, "inquiries/inquiry_detail.html", {"inquiry": inquiry})


# inquiriesの作成
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR])
def inquiry_create(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inquiry_list")
    else:
        form = InquiryForm()
    return render(request, "inquiries/inquiry_create.html", {"form": form})


# inquiriesの編集
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR])
def inquiry_update(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    if request.method == "POST":
        form = InquiryForm(request.POST, instance=inquiry)
        if form.is_valid():
            form.save()
            return redirect("inquiry_detail", pk=pk)
    else:
        form = InquiryForm(instance=inquiry)
    return render(
        request, "inquiries/inquiry_update.html", {"form": form, "inquiry": inquiry}
    )


# inquiriesの削除
@login_required
@role_required([UserRole.ADMIN, UserRole.EDITOR])
def inquiry_delete(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    if request.method == "POST":
        inquiry.delete()
        return redirect("inquiry_list")
    return render(request, "inquiries/inquiry_delete.html", {"inquiry": inquiry})
