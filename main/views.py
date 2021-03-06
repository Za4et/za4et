import os
import zipfile
from io import BytesIO

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.encoding import smart_str

from Za4et.settings import BASE_DIR
from main.models import News, Files, Discipline, Group, Student, Journal


def index(request):
    return render(request, 'zach/home.html')


def start(request):
    return render(request, 'zach/start.html')


def news(request):
    news = {'news': News.objects.all()}
    return render(request, 'zach/news.html', news)


@login_required
def account(request):
    if request.method == 'POST':
        student = Student.objects.get(username=request.user)
        try:
            student.background_image = request.FILES['profile_backg']
            student.save()
        except MultiValueDictKeyError:
            student.avatar = request.FILES['profile_photo']
            student.save()
    user = Student.objects.filter(username=request.user).values('group__journal__link', 'fio', 'group__name',
                                                                'background_image',
                                                                'place_of_styding', 'avatar')
    return render(request, 'zach/account.html', {'accounts': user})


def journals(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        groups = Group.objects.filter(name__icontains=search).values('name', 'journal__link')
        return render(request, 'zach/left_menu/journals.html', {'search_groups': groups, 'search': search})
    else:
        return render(request, 'zach/left_menu/journals.html',
                      {'groups': Group.objects.all().values('name', 'journal__link')})


def library(request):
    if request.method == 'POST':
        try:
            if request.POST['file'] == 'true':
                file_names = []
                files = dict(request.POST)['foo']
                for i in files:
                    file_names.append(BASE_DIR + i)
                for file in file_names:
                    response = HttpResponse(content_type='application/force-download')
                    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file)
                    response['X-Sendfile'] = smart_str(file)
                    return response
        except:
            file_names = []
            files = dict(request.POST)['foo']
            for i in files:
                file_names.append(BASE_DIR + i)
            zip_subdir = request.POST['discipline']
            zip_filename = "%s.zip" % zip_subdir
            s = BytesIO()
            zf = zipfile.ZipFile(s, "w")

            for f_path in file_names:
                fdir, fname = os.path.split(f_path)
                zip_path = os.path.join(zip_subdir, fname)
                zf.write(f_path, zip_path)
            zf.close()
            resp = HttpResponse(s.getvalue(), content_type="application/x-zip-compressed")
            resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

            return resp

    if request.GET.get('search'):
        search = request.GET.get('search')
        materials = Files.objects.filter(Q(name__icontains=search) |
                                         Q(tag__name__icontains=search) |
                                         Q(discipline__name__icontains=search) |
                                         Q(teacher__fio__icontains=search))
        return render(request, 'zach/left_menu/library.html', {'materials': materials, 'search': search})
    else:
        disciplines = Discipline.objects.all()
        return render(request, 'zach/left_menu/library.html', {'disciplines': disciplines.order_by('name')})


def questions(request):
    return render(request, 'zach/right_menu/questions.html')


def information(request):
    return render(request, 'zach/right_menu/information.html')


def article(request, year, month, day, slug):
    article = get_object_or_404(News, published__year=year, published__month=month, published__day=day, slug=slug)
    return render(request, 'zach/article.html', {'article': article})


def tag(request, tag_name):
    return render(request, 'zach/news.html', {'news': News.objects.filter(category__title=tag_name)})


def get_files(request):
    file_names = [BASE_DIR + "/tmp/file1.txt", BASE_DIR + "/tmp/file2.txt"]
    zip_subdir = 'some_files'
    zip_filename = "%s.zip" % zip_subdir
    s = BytesIO()
    zf = zipfile.ZipFile(s, "w")

    for f_path in file_names:
        fdir, fname = os.path.split(f_path)
        zip_path = os.path.join(zip_subdir, fname)
        zf.write(f_path, zip_path)
    zf.close()
    resp = HttpResponse(s.getvalue(), content_type="application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp


def logn(request):
    if request.recaptcha_is_valid:
        user = request.POST['login']
        password = request.POST['pass']
        user = authenticate(username=user, password=password)
        login(request, user)
        return redirect('/account/')


from django.http import Http404


def res_search(request):
    search_list = {}
    if request.GET.get('main_search'):
        if request.GET.get('news'):
            news_check = True
            news = request.GET.get('main_search')
            news_list = News.objects.filter(Q(title__icontains=news) |
                                            Q(text__icontains=news) |
                                            Q(institute__name__icontains=news) |
                                            Q(category__title__icontains=news)

                                            )
            search_list['new_on'] = news_check
            search_list['news'] = news_list
        if request.GET.get('library'):
            library_check = True
            library = request.GET.get('main_search')
            materials = Files.objects.filter(Q(name__icontains=library) |
                                             Q(tag__name__icontains=library) |
                                             Q(discipline__name__icontains=library) |
                                             Q(teacher__fio__icontains=library))
            search_list['materials'] = materials
            search_list['library_on'] = library_check
        if request.GET.get('journals'):
            groups_check = True
            journals = request.GET.get('main_search')
            group_list = Journal.objects.filter(Q(group__name__icontains=journals) |
                                                Q(discipline__name__icontains=journals)
                                                ).values('link', 'group__name', 'group__slug')
            search_list['groups'] = group_list
            search_list['groups_on'] = groups_check

        return render(request, 'zach/res_search.html', search_list)
    else:
        return Http404
