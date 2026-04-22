from django.db import models

from core.softdelete import SoftDeleteModel, SoftDeleteManager


# Create your models here.



class Hashtags(SoftDeleteModel):
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

    class Meta:
        
        db_table = 'hashtags'

        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtags'
        
