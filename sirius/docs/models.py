from django.utils import timezone
from django.db import models


class Employee(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    full_name = models.CharField(max_length=120, null=False)
    birthday = models.DateField()
    position = models.CharField(max_length=120, null=True)

    def __str__(self):
        return f'{self.full_name}'


class Document(models.Model):
    class Meta:
        verbose_name = 'Документ',
        verbose_name_plural = 'Документы'

    work_doc = 'WD'
    dismissal = 'DM'
    choice_doc = [
        (work_doc, 'Справка с места работы'),
        (dismissal, 'Увольнение')
    ]

    type_doc = models.CharField(max_length=2, choices=choice_doc, default=work_doc)
    addressee = models.ManyToManyField(Employee)
    doc_direction = models.CharField(max_length=120, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.pk}, {self.type_doc}'
