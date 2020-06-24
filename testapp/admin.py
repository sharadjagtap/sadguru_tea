from django.contrib import admin

# Register your models here.


from testapp.models import Tea

class TeaAdmin(admin.ModelAdmin):
    list_display = ['name','description','price']

admin.site.register(Tea,TeaAdmin)