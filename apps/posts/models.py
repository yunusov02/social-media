from django.db import models
from django.conf import settings
from core.softdelete import SoftDeleteModel, SoftDeleteManager
from apps.hashtags.models import Hashtags

class Post(SoftDeleteModel):
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='posts'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtags, related_name='posts', blank=True)

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f"{self.user.username} - {self.title[:20]}"