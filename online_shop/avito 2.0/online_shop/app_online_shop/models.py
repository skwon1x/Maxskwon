from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from online_shop.settings import STATIC_URL

# Create your models here.

User = get_user_model()

# Создаём класс с описанием структуры таблицы (наследование от model)
class OnlineShop(models.Model):
    # создаём заголовок
    title = models.CharField('Заголовок', max_length=128)
    # Описание
    # TextField - строковое поле большого размера
    description = models.TextField('Описание')
    # decimal как float
    # decimal_places колво знаков после запятой
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    auction = models.BooleanField('Торг', help_text='Укажите, уместен ли торг')

    # auto_now_add автополучение даты при создании auto_now при добавлении
    created_time = models.DateTimeField('Дата создания', auto_now_add=True)

    updated_time = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    image = models.ImageField(verbose_name='Изображение', upload_to='online_shop/', blank=True)

    # Создаем функцию для столбца 'Дата создания' админки
    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_time.date() == timezone.now().date():
            created_time = self.created_time.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_time.strftime("%d.%m.%Y в %H:%M:%S")
    
    # Создаем функцию для столбца 'Дата обновления' админки    
    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_time.date() == timezone.now().date():
            updated_time = self.updated_time.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: orange; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.updated_time.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='Предпросмотр изображения')
    def preview_img(self): 
        # Если есть картинка, то покажем ее
        if self.image:
            return format_html('''
                                    <a href="{}"><img src="{}" height=150 width=250></a>
                               ''',
                                self.image.url,
                                self.image.url
            )
        # Если картинки нет то покажем картинку по умолчанию
        else:
            # Наверно можно добраться до static из admin проще, но я не нашел как...
            # Если можно, подскажите... :)
            img_url = f"../../../{STATIC_URL}img/shop.png"
            return format_html('''
                                    <a href="{}"><img src="{}" height=150 width=250></a>
                                ''',
                                img_url,
                                img_url
            )
        
    class Meta():
        db_table = 'advertisements'

    def __str__(self):
        return f'id={self.id}, title={self.title}, price={self.price}'