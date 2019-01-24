from django.contrib import admin

# Register your models here.
from .models import Character


class CharacterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('civility'), ('first_name', 'last_name'),)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('user',)
        })
    )
    list_display = (
        'id', 'first_name', 'last_name',
    )
    # list_editable = ('civility', 'email', 'phone', 'cellphone')


admin.site.register(Character, CharacterAdmin)
