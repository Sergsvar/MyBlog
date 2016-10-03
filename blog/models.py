from django.db import models
from django.utils import timezone

class Post(models.Model):
    head = models.CharField(max_length=250, verbose_name=u'Заголовок')
    text = models.TextField(verbose_name=u'Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name=u'Дата создания')
    tags = models.CharField(max_length=250, verbose_name=u'Теги через пробел')

    class Meta:
        verbose_name_plural = 'Статьи'
    def __str__(self):
        return self.head

    def getTags(self):
        self.lst = self.tags.split()
        return self.lst

    def shortText(self):
        if len(self.text)>150:
            return self.text[:500]
