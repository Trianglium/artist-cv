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
        return format_html('<div class="container-xs {}">', extra_classes)
    elif bool(fluid)==True:
        return format_html('<div class="container-fluid {}">', extra_classes)

@register.simple_tag
def endcontainer():
    return format_html("</div>")
