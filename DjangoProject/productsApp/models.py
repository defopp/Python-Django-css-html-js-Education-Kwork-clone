from django.db import models

# Create your models here.
class MainCategory(models.Model):
    name = models.CharField(max_length = 50, blank = False, unique = True)
    urlname = models.CharField(max_length = 20, blank = False)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length = 50, blank = False, unique = True)
    urlname = models.CharField(max_length = 20, blank = False)
    def __str__(self):
        return self.name
    
class DetailCategory(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length = 50, blank = False, unique = True)
    urlname = models.CharField(max_length = 20, blank = False)
    def __str__(self):
        return self.name
    
class Product():
    pass