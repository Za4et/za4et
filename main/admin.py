from django.contrib import admin

# Register your models here.
from main.models import News, Category, Institute, Files, Teacher, TagFiles, Discipline, Journal, Group, FormStyding, \
    Task, Executor, Student

admin.site.register(News)


@admin.register(TagFiles)
class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Discipline)
admin.site.register(Category)
admin.site.register(Student)
admin.site.register(Task)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(FormStyding)


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['group', 'discipline']


@admin.register(Institute)
class InstAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


@admin.register(Files)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']
    list_filter = ('teacher__fio', 'tag__name',)
    search_fields = ['name', 'teacher__fio']
