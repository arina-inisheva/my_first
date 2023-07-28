from django.db import models

# Create your models here.

class Advertisement(models.Model):
    def __str__(self):
        return f'id={self.id}, title={self.title}, price={self.price}'

    title = models.CharField('название', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена',max_digits=12, decimal_places=2 )
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "advertisements"