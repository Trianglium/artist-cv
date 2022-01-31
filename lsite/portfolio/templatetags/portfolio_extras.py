from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from portfolio.models import Project


register = template.Library()

# Rows
@register.simple_tag
def row(extra_classes=''):
    return format_html('<div class="row {}">', extra_classes)

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


# iFrames for Urls
@register.simple_tag
def iframe(link='', width='100%', height='100%', fborder='0', trans='true'):
    return format_html('<iframe src="{}" width="{}" height="{}" frameBorder="{}" allowtransparency="{}" allow="encrypted-media"></iframe>', link, width, height, fborder, trans)
