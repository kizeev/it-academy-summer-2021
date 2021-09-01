from django.db import models


class Category(models.Model):
    """Модель представляет категории, на которые делятся задачи."""
    category_name = models.CharField(
        max_length=20,
        help_text='укажите категорию задачи',
        verbose_name='Категория'
    )

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Строка для представления названия категории."""
        return self.category_name


class Task(models.Model):
    """Модель представляет задачу, которую планируется выполнить."""
    PRIORITY_CHOICES = (
        ('high', 'Высокий'),
        ('medium', 'Средний'),
        ('low', 'Низкий'),
    )
    task_name = models.CharField(max_length=40, help_text='что нужно', verbose_name='Задача')
    task_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        help_text='выберите категию задачи',
        verbose_name='Категория',
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='low',
        verbose_name='Приоритет'
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        """Строка для представления задачи."""
        return self.task_name
