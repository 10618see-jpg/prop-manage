from webbrowser import get

from django.db import models


# Create your models here.
# 共通モデル ------------------------------
class Property(models.Model):
    # 物件種別
    class PropertyType(models.TextChoices):
        LAND = "LAND", "土地"
        BUILDING = "BUILDING", "建物"
        COND = "COND", "マンション"

    # 物件所在地
    city = models.CharField(max_length=100, db_index=True)
    town = models.CharField(max_length=100, db_index=True)
    street = models.CharField(
        max_length=100,
    )  # 番地

    # 緯度・経度
    latitude = models.FloatField()
    longitude = models.FloatField()

    # 価格
    price = models.DecimalField(max_digits=12, decimal_places=2, db_index=True)

    # 登録日
    registration_date = models.DateField(auto_now_add=True)

    # ステータス
    class PropertyStatus(models.TextChoices):
        AVAILABLE = "AVAILABLE", "公開中"
        PENDING = "PENDING", "商談中"
        SOLD = "SOLD", "売約済み"
        HIDDEN = "HIDDEN", "非公開"

    # PropertyTypeフィールド
    property_type = models.CharField(
        max_length=10,
        choices=PropertyType.choices,
        default=PropertyType.LAND,
        db_index=True,
    )

    # PropertyStatusフィールド
    property_status = models.CharField(
        max_length=10,
        choices=PropertyStatus.choices,
        default=PropertyStatus.AVAILABLE,
        db_index=True,
    )

    # ユーザーへの外部キー、on_delete=SET_NULL
    manager = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="properties",
    )

    # 売主への外部キー、on_delete=PROTECT
    seller = models.ForeignKey(
        "customers.Customer",
        on_delete=models.PROTECT,
        related_name="properties",
    )


# landモデル　------------------------------
class Land(Property):
    # 土地面積
    area = models.DecimalField(
        max_digits=10, decimal_places=2, db_index=True
    )  # 土地面積

    # 地目
    class LandCategory(models.TextChoices):
        RESIDENTIAL = "RESIDENTIAL", "宅地"
        AGRICULTURAL = "AGRICULTURAL", "農地"
        FOREST = "FOREST", "山林"
        OTHER = "OTHER", "その他"

    # 建ぺい率
    building_coverage_ratio = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    # 容積率
    floor_area_ratio = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    # 権利形態
    class LandRightType(models.TextChoices):
        OWNERSHIP = "OWNERSHIP", "所有権"
        LEASEHOLD = "LEASEHOLD", "借地権"
        OTHER = "OTHER", "その他"

    # LandCategoryフィールド
    land_category = models.CharField(
        max_length=20,
        choices=LandCategory.choices,
        default=LandCategory.RESIDENTIAL,
    )

    # LandRightTypeフィールド
    land_right_type = models.CharField(
        max_length=20,
        choices=LandRightType.choices,
        default=LandRightType.OWNERSHIP,
    )

    # 面積計算（㎡→坪）
    @property
    def area_tsubo(self):
        return self.area / 3.30578


# buildingモデル ------------------------------
class Building(Property):
    # 建物面積
    area = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)

    # 構造
    class BuildingStructure(models.TextChoices):
        WOOD = "WOOD", "木造"
        S = "S", "鉄骨造"
        RC = "RC", "鉄筋コンクリート造"
        SRC = "SRC", "鉄骨鉄筋コンクリート造"
        OTHER = "OTHER", "その他"

    # 建物構造フィールド
    building_structure = models.CharField(
        max_length=20,
        choices=BuildingStructure.choices,
        default=BuildingStructure.WOOD,
        db_index=True,
    )

    # 築年月
    build_year = models.IntegerField(verbose_name="築年（西暦）", null=True, blank=True)
    build_month = models.IntegerField(verbose_name="築月", null=True, blank=True)

    # 建物の築年数を計算するプロパティ
    @property
    def age(self):
        from datetime import date

        if self.build_year and self.build_month:
            today = date.today()
            age = today.year - self.build_year
            if today.month < self.build_month:
                age -= 1
            return age
        return None

    # 間取り
    floor_plan = models.CharField(max_length=20, blank=True)

    # 接道状況
    road_access = models.CharField(max_length=20, blank=True)


# condモデル ------------------------------
class Cond(Property):
    # 専有面積
    area = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)

    # マンション名
    condominium_name = models.CharField(max_length=100)

    # 部屋番号
    room_number = models.CharField(max_length=20)

    # 階数
    floor = models.IntegerField()

    # 管理費・修繕積立金
    management_fee = models.DecimalField(max_digits=12, decimal_places=2)
    maintenance_fee = models.DecimalField(max_digits=12, decimal_places=2)

    # ペット可否
    class PetPolicy(models.TextChoices):
        ALLOWED = "ALLOWED", "可"
        NOT_ALLOWED = "NOT_ALLOWED", "不可"
        NEGOTIABLE = "NEGOTIABLE", "要相談"

    # ペット可否フィールド
    pet_policy = models.CharField(
        max_length=20,
        choices=PetPolicy.choices,
        default=PetPolicy.NOT_ALLOWED,
        db_index=True,
    )

    # 管理形態
    class ManagementType(models.TextChoices):
        SELF_MANAGED = "SELF_MANAGED", "自主管理"
        CONTRACTED = "CONTRACTED", "委託管理"
        OTHER = "OTHER", "その他"

    # 管理形態フィールド
    management_type = models.CharField(
        max_length=20,
        choices=ManagementType.choices,
        default=ManagementType.CONTRACTED,
    )


def __str__(self):
    return f"{self.city} {self.town} {self.street} ({self.get_property_type_display()})"
