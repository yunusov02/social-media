from django.db import models
from django.utils import timezone



class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    def hard_delete(self):
        super().delete()




class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        self.update(is_deleted=True, deleted_at=timezone.now())

    def restore(self):
        self.update(is_deleted=False, deleted_at=None)

    def hard_delete(self):
        super().delete()




class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(is_deleted=False)

    def deleted(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(is_deleted=True)





"""

To apply all of them to our models 


class Post(SoftDeleteModel):
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    title = models.CharField(max_length=100)
    content = models.TextField()
    ...

"""
