from django.db import models
from django.urls import reverse


class Phone(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, verbose_name='Брэнд')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Телефоны'
        verbose_name_plural = 'Телефоны'
        ordering = ['time_create', 'title']


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Бренд')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand', kwargs={'brand_id': self.pk})

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['id']