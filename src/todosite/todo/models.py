from django.db import models


class CategoryTask(models.Model):
    """Модель представляет категории, на которые делятся задачи"""
    category_name = models.CharField(max_length=20, help_text='укажите категорию задач')

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
    task_name = models.CharField(max_length=40, help_text='что нужно')
    category_task = models.ForeignKey(
        CategoryTask,
        on_delete=models.SET_NULL,
        null=True,
        help_text='выберите категию задачи',
    )
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        """Строка для представления задачи."""
        return self.task_name
