from django.contrib import admin
from app_music.models import (
Artist,
Album,
Track,
Tag
)
# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Tag)
