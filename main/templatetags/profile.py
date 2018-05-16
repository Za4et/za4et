from django import template

from main.models import Student

register = template.Library()


@register.simple_tag(takes_context=True)
def get_full_name(context):
    request_user = context.request.user
    if request_user.is_superuser == False:
        acc = Student.objects.get(username=context.request.user)
        return acc.fio
