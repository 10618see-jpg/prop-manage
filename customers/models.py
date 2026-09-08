from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100) #氏名
    email = models.EmailField(blank=True, null=True) #メールアドレス
    phone_number = models.CharField(max_length=20, blank=True, null=True) #電話番号
    address = models.TextField(blank=True, null=True) #住所
    created_at = models.DateTimeField(auto_now_add=True) #作成日時
    free_text = models.TextField(blank=True, null=True) #備考欄

def __str__(self):
    return self.name
