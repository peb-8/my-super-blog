from django.db import models

from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Journey(TimeStampedModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="journeys",
    )

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    journey = models.ForeignKey(
        Journey, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="posts"
    )
    image_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="posts",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/post/%i/" % self.id

    @staticmethod
    def find(author_username):
        return Post.objects.find(created_by__username=author_username)
