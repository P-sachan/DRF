from django.contrib import admin
from .models import File

# Register your models here.
@admin.register(File)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['id']