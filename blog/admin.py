from django.contrib import admin

# Register your models here.
from blog.models import Post,Contact,Comment
admin.site.register((Post,Contact,Comment))