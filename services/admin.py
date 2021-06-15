from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Service, Component

# Register your models here.


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Service, SomeModelAdmin)
admin.site.register(Component, SomeModelAdmin)
