from django.contrib import admin
from main.models import Testimonial, Author, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Testimonial)

admin.site.register(Author, SomeModelAdmin)

admin.site.register(Contact)
