from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from projects.models import Project


register = template.Library()

# Rows
@register.simple_tag
def row(extra_classes=''):
    return format_html('<div class="row {} m-2 p-2">', extra_classes)

@register.simple_tag
def endrow():
    return format_html("</div>")


# Columns
@register.simple_tag
def col(extra_classes=''):
    return format_html('<div class="col {}">', extra_classes)

@register.simple_tag
def endcol():
    return format_html("</div>")

# Container
@register.simple_tag
def container(extra_classes='', fluid=False):
    if bool(fluid)==False:
        return format_html('<div class="container-xs {} m-2 p-2">', extra_classes)
    elif bool(fluid)==True:
        return format_html('<div class="container-fluid {}">', extra_classes)

@register.simple_tag
def endcontainer():
    return format_html("</div>")


@register.simple_tag
def title_subtitle(title="", subtitle=""):
    return format_html('<p class="display-1">{}</p><p class="h4"><small class="text-muted">{}</small></p>', title, subtitle)



# <span class="material-icons-outlined">pause_circle_outline</span>
@register.simple_tag
def media_icon(post=""):
    media_key = {'audio':'<span class="material-icons-outlined">play_circle_outline</span>', 'image':'<span class="material-icons-outlined">photo</span>', 'video':'<span class="material-icons-outlined">ondemand_video</span>' }
    for mtype in media.keys():
        if mtype in post:
            return format_html(media[k])
    return None










