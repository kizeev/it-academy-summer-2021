from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Category(models.Model):
    """Модель представляет категории, на которые делятся задачи."""
    category_name = models.CharField(
        max_length=20,
        help_text='укажите категорию задачи',
        verbose_name='Категория'
    )

    def get_absolute_url(self):
        return reverse('tasks_by_category', kwargs={'category_id': self.pk})

    class Meta:
        """Класс, описывающий отображение категории."""
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
    due_date = models.DateField(null=True, blank=True, verbose_name='Срок выполнения')
    notes = models.CharField(max_length=250, verbose_name='заметки', blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='low',
        verbose_name='Приоритет'
    )
    completed = models.BooleanField(verbose_name='Завершено', default=False, blank=True)
    tags = TaggableManager(blank=True)

    class Meta:
        """Класс, описывающий отображение задачи."""
        ordering = ['-created']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        """Строка для представления задачи."""
        return self.task_name

    def get_absolute_url(self):
        return reverse('view_task', kwargs={'task_id': self.pk})
