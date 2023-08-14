from django.contrib import admin
from .models import Advertisement
from django.utils.html import  format_html
from django.utils import timezone

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "date_of_create", "updated_date", "auction"]
    list_filter = ["auction", "created_at"]
    actions = ["make_auction_as_false", "make_auction_as_true" ]

    @admin.display(description = 'Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            creted_time = self.created_at.time().strtime('%H:%M:%S')
            return format_html('<span style = "color: green; front-weight:bold;">Сегодня в {}</span>')
    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
       queryset.update(auction = False)

       @admin.action(description='добавить возможность торга')
       def make_auction_as_true(self, request, queryset):
          queryset.update(auction=True)

admin.site.register(Advertisement,AdvertisementAdmin)