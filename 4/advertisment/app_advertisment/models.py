from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.html import format_html


# Create your models here.

class Advertisement(models.Model):
    title = models.CharField('название', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=12, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strtime('%H:%M:%S')
            return format_html('<span style = "color: green; front-weight:bold;">Сегодня в {}</span>', created_time)
        return self.created_at

    def __str__(self):
        return f"Adverisement(id={self.id}, title={self.title}, price={self.price}"


class Meta:
    db_table = "advertisement"
