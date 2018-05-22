from django import template

from main.models import Student, Group

register = template.Library()


@register.simple_tag(takes_context=True)
def get_full_name(context):
    request_user = context.request.user
    if request_user.is_superuser == False:
        acc = Student.objects.get(username=context.request.user)
        return acc.fio


@register.simple_tag(takes_context=True)
def permissions_group(context, context_group, link):
    request_user = context.request.user
    student = Student.objects.get(username=request_user)
    try:
        group = Group.objects.get(student__fio=student.fio)
        if str(context_group) == str(group):
            return str('href=' +link + ' '+'target=jframe')
        else:
            return 'href=#'
    except:
        return '#'
