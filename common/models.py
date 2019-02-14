from django.db import models


class Base(models.Model):
    draw = models.IntegerField(blank=True, null=True)
    draw_date = models.DateField(blank=True, null=True)
    num1 = models.IntegerField(blank=True, null=True)
    num2 = models.IntegerField(blank=True, null=True)
    num3 = models.IntegerField(blank=True, null=True)
    num4 = models.IntegerField(blank=True, null=True)
    num5 = models.IntegerField(blank=True, null=True)
    num6 = models.IntegerField(blank=True, null=True)
    powerball = models.IntegerField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'base'
        verbose_name = 'base'
        verbose_name_plural = verbose_name


class Population(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True) # : : : 형식
    counts = models.IntegerField()
    depth = models.IntegerField()  # 2::::: 일 경우 1, 2:4:::: 일 경우 2
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table = 'populations'
        verbose_name = 'populations'
        verbose_name_plural = verbose_name