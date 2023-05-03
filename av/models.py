from django.db import models

class Product(models.Model):
    model = models.TextField(
        verbose_name="Модель авто",
    )
    marka = models.TextField(
        verbose_name="Марка авто",
    )
    price = models.IntegerField(
        verbose_name="Цена, $",
    )
    year = models.IntegerField(
        verbose_name="Год выпуска автомобиля",
    )
    url = models.URLField(
        verbose_name="URL адрес объявления",
        unique=True,
        default='None',
    )

    def __str__(self):
        return f'#{self.pk} {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
