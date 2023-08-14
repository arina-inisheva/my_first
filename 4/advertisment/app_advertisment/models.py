from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('название', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=12, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisments/')
    @admin.display(description='Дата создания')
    def date_of_create(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style = "color: green; front-weight:bold;">Сегодня в {}</span>', created_time)
        return self.created_at

    @admin.display(description='Дата обновления')
    def updated_date(self):
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html('<span style = "color: blue; front-weight:bold;">Сегодня в {}</span>', updated_time)
        return self.update_at
    def __str__(self):
        return f"Adverisement(id={self.id}, title={self.title}, price={self.price}"


class Meta:
    db_table = "advertisement"
