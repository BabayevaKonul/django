import datetime

from django.db import models
from django.utils import timezone


class Sual(models.Model):
    sual_metni = models.CharField(max_length=200)
    qeydiyyat_tarixi = models.DateTimeField("qeydiyyat zamani")
    def __str__(self):
        return self.sual_metni

    def yeni_elave_edilen(self):
        return self.qeydiyyat_tarixi >= timezone.now() - datetime.timedelta(days=1)

class sechim(models.Model):
    sual = models.ForeignKey(Sual, on_delete=models.CASCADE)
    sechim_metni= models.CharField(max_length=200)
    sesler = models.IntegerField(default=0)
    def __str__(self):
        return self.sechim_metni
# Create your models here.
