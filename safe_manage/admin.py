from django.contrib import admin

# Register your models here.

from safe_manage.models import Examination,Problem,Rectification,Comment
admin.site.register(Examination)
admin.site.register(Problem)
admin.site.register(Rectification)
admin.site.register(Comment)
