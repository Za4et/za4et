# Create your views here.
from django.http import JsonResponse
from django.utils.encoding import smart_str

from main.models import News, Institute, Group, Files


def get_news(request, institute):
    institute = smart_str(institute)
    text_list = []
    image_list = []
    tag_list = []
    title_list = []
    date_list = []
    url_list = []

    if institute == 'all':
        news = News.objects.all()
    else:
        inst = Institute.objects.get(slug=str(institute))
        news = News.objects.filter(institute=inst)

    for new in news:
        cat_list = []
        text_list.append(new.text)
        image_list.append(new.image.url)
        for cat in new.category.all():
            cat_list.append(str('<a href="/tag/' + cat.title + '">' + '#' + cat.title + '</a>'))
            tag_list.append(cat_list)
            title_list.append(new.title)
            date_list.append(new.published)
            url_list.append(new.get_absolute_url())

    data = {
        'text': text_list,
        'tag': tag_list,
        'title': title_list,
        'url': url_list,
        'image': image_list,
        'date': date_list

    }
    return JsonResponse(data)


def get_journals(request, institute, form_edu, course):
    groups_list = []
    link_list = []
    groups = Group.objects.filter(institute__slug=institute, form_edu__name=form_edu, cource=course).values('name',
                                                                                                            'journal__link')
    for group in groups:
        groups_list.append(group['name'])
        link_list.append(group['journal__link'])
    data = {'links': link_list,
            'groups': groups_list,
            }
    return JsonResponse(data)


def get_materials(request, discipline):
    material_list = []
    material_name_list = []
    disciplines = Files.objects.filter(discipline__name=discipline)
    for discipline in disciplines:
        material_list.append(discipline.file.url)
        material_name_list.append(discipline.name)
    data = {'file_urls': material_list,
            'names': material_name_list}
    return JsonResponse(data)
