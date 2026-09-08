from django.db import models


# Create your models here.
# 物件への外部キー
class Contract(models.Model):
    target_property = models.ForeignKey(
        "properties.Property",
        on_delete=models.PROTECT,
        related_name="contracts",
    )

    # 顧客への外部キー
    target_customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.PROTECT,
        related_name="contracts",
    )

    # ユーザーへの外部キー
    target_accounts = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, related_name="contracts", null=True
    )

    # 売買価格
    contract_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    # 契約日
    contract_date = models.DateField()

    # 引き渡し日
    handover_date = models.DateField()

    # 進捗ステータス
    class Status(models.TextChoices):
        PREPARING = "PREPARING", "契約前"
        SIGNED = "SIGNED", "契約締結"
        REVIEWING = "REVIEWING", "ローン審査"
        COMPLETED = "COMPLETED", "決済・引渡"
        CANCELED = "CANCELED", "キャンセル・破談"

    # Statusフィールド
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PREPARING,
    )
