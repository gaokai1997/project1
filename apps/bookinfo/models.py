from django.db import models

# Create your models here.
from django.db import models
class libray(models.Model):
    CHOISE_CATEGORY=((0,"经济金融"),(1,"教育考试"),(2,"计算机与网络"),(3,"语言学习"),(4,"其他"))
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20,verbose_name="书名")
    author=models.CharField(max_length=20,verbose_name="作者")
    pub_host=models.CharField(null=True,verbose_name="发布人",max_length=20)
    category=models.SmallIntegerField(choices=CHOISE_CATEGORY,default=4,verbose_name="类别")
    pub_date=models.DateField(null=True,verbose_name="发布日期")
    count=models.IntegerField(null=True,verbose_name="数量")
    abradability=models.IntegerField(null=True,verbose_name="新旧程度")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="单价")
    image=models.ImageField(null=True,verbose_name="图片")
    class Meta:
        db_table = 'tb_librayr'
        verbose_name = '图书'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name