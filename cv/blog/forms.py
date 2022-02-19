from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from blog.models import Comment, Post, Tag, AuthorProfile


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["content"]

  def __init__(self, *args, **kwargs):
    super(CommentForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ["title", "summary", "content", "tags"]

class TagForm(forms.ModelForm):
  class Meta:
    model = Tag
    fields = ["value"]

class AuthorProfileForm(forms.ModelForm):
    class Meta:
        model = AuthorProfile
        fields = ["bio"]
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.formfield_for_manytomany
