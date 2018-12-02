#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SparepartCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sortorder = models.IntegerField(blank=True, null=True)
    activestate = models.IntegerField(db_column='activeState')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dt_sparepart_categories'


class Sparepart(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    categoryid = models.IntegerField(db_column='categoryId')  # Field name made lowercase.
    productcode = models.CharField(max_length=20, db_column='productCode')  # Field name made lowercase.
    revision = models.CharField(max_length=30)
    imagefile = models.TextField(db_column='imageFile')  # Field name made lowercase.
    genericprice = models.FloatField(db_column='genericPrice')  # Field name made lowercase.
    zebraprice = models.FloatField(db_column='zebraPrice')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dt_spareparts'


class SpmStockItem(models.Model):
    stockid = models.IntegerField(db_column='stockId')  # Field name made lowercase.
    sparepartid = models.IntegerField(db_column='sparePartId')  # Field name made lowercase.
    minlevel = models.IntegerField(db_column='minLevel')  # Field name made lowercase.
    maxlevel = models.IntegerField(db_column='maxLevel')  # Field name made lowercase.
    stockamount = models.IntegerField(db_column='stockAmount')  # Field name made lowercase.
    binlocator = models.CharField(db_column='binLocator', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dt_spm_stock_items'


class SpmStock(models.Model):
    title = models.TextField()
    description = models.TextField()
    prio = models.IntegerField()
    allowedusers = models.TextField(db_column='allowedUsers')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dt_spm_stocks'


# Create your models here.
