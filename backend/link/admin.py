from django.contrib import admin
from link.models import Link

# Register your models here.


@admin.register(Link)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'long_url', 'short_url')
    fields = ('long_url',)
    readonly_fields = ()
