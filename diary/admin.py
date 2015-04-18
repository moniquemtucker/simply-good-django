from django.contrib import admin

# Register your models here.

from diary.models import DiaryEntry

admin.site.register(DiaryEntry)