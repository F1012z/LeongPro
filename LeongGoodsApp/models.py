from django.db import models
import datetime
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    address = RichTextUploadingField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = RichTextUploadingField()
    pic = RichTextUploadingField(default=0)
    pi = RichTextUploadingField(default=0)
    isDelete = models.BooleanField(default=False)
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gtype = models.ForeignKey(TypeInfo)
    gclick = models.IntegerField(default=0)
    gunit = models.CharField(max_length=20, default='500g')
    gjianjie = models.TextField()
    gpub_date = models.DateTimeField(datetime.datetime.now())
    gpubj_date = models.DateTimeField()

    def __str__(self):
        return self.gtitle
