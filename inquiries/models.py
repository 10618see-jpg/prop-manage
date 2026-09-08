from django.db import models


# Create your models here.
# 顧客への外部キー（on_delete=CASCADE）
class Inquiry(models.Model):
    target_customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        related_name="inquiries",
    )

    # 物件への外部キー（on_delete=CASCADE）
    target_property = models.ForeignKey(
        "properties.Property",
        on_delete=models.CASCADE,
        related_name="inquiries",
    )

    # 種別
    class InquiryType(models.TextChoices):
        INQUIRY = "INQUIRY", "問い合わせ"
        SHOWING_REQUEST = "SHOWING_REQUEST", "内覧希望"
        PURCHASE_INTENT = "PURCHASE_INTENT", "購入申込"
        PRICE_NEGOTIATION = "PRICE_NEGOTIATION", "価格交渉"

    # InquiryTypeフィールド
    inquiry_type = models.CharField(
        max_length=20,
        choices=InquiryType.choices,
        default=InquiryType.INQUIRY,
    )

    inquiry_date = models.DateTimeField(auto_now_add=True)  # 問い合わせ日時
    inquiry_text = models.TextField(blank=True)  # 問い合わせ内容
    # カスタマーアプリを参照するために、Customerモデルを外部キーとして設定しています。
    # プロパティアプリを参照するために、Propertyモデルを外部キーとして設定しています。
