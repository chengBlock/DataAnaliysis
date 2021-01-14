from django.db import models


# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    pwd = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id) + "-" + self.username


class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20,decimal_places=5)
    number = models.IntegerField()
    is_sale_off = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return str(self.id) + "-" + self.goods_name + "-" +self.date


class Custom(models.Model):
    id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20,decimal_places=5)
    address = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return str(self.id) + "-" + self.goods_name + "-" + self.date


# 商品A的历史记录，价格，销售量，销售日期
class AGR(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=20, decimal_places=5)
    number = models.IntegerField()
    date = models.DateField()


class BGR(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=20, decimal_places=5)
    number = models.IntegerField()
    date = models.DateField()


class CGR(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=20, decimal_places=5)
    number = models.IntegerField()
    date = models.DateField()


class DGR(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=20, decimal_places=5)
    number = models.IntegerField()
    date = models.DateField()


class EGR(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=20, decimal_places=5)
    number = models.IntegerField()
    date = models.DateField()
