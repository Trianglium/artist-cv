from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from base.models import BaseContent, BaseArticle



class Comment(BaseContent):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.creator

class Tag(models.Model):
    value = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.value


class Post(BaseArticle):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    # db_index is required. do not remove.
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title
# AuthorProfile as to separate info from the User Auth Model
# Allowing for a separation of concerns
# And added security.
class AuthorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField(
        null=True,
        blank=True,
        help_text='Optional Author Bio. Separate From Professional Profile Resume Summary and Object',
    )

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"