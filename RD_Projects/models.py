from django.db import models
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
# Create your models here.


class productDomain(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class serviceDomain(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='images/Project_pics', null=True, blank=True)
    video = models.FileField(upload_to='images/Project_videos', null=True, blank=True)
    voucher = models.ImageField(upload_to='images/Project_vouchers', null=True, blank=True)
    voucherPDF = models.FileField(upload_to='images/Project_voucherPDF', null=True, blank=True)
    domain = models.ForeignKey(productDomain, default=1, on_delete=models.CASCADE)
    content = RichTextField()


class Service(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='images/Service_pics', null=True, blank=True)
    voucher = models.ImageField(upload_to='images/Service_vouchers', null=True, blank=True)
    voucherPDF = models.FileField(upload_to='images/Service_voucherPDF', null=True, blank=True)
    domain = models.ForeignKey(serviceDomain, default=1, on_delete=models.CASCADE)
    content = RichTextField()

