from django.contrib import admin
from . import models


# Register your models here.
# admin.site.register(models.TypeInfo)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'address')


admin.site.register(models.TypeInfo, TypeAdmin)


class GoodAdmin(admin.ModelAdmin):
    list_display = ('gtitle', 'gpic', 'gprice', 'gclick', 'gunit',)
    list_filter = ('gpub_date', 'gprice')
    search_fields = ('gtitle', 'gclick')
    date_hierarchy = 'gpub_date'
    ordering = ['gpub_date', 'gclick']


admin.site.register(models.GoodsInfo, GoodAdmin)
