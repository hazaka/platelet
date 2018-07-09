from django.db import models
from django.db.models import Manager


class Name(models.Model):
    text = models.CharField(max_length=255)
    language = models.ForeignKey('utils.Language', null=True)
    is_default = models.BooleanField(default=False)

    @staticmethod
    def get_default_name(names: Manager):
        return names.filter(is_default=True).first()

    def __str__(self):
        return self.text


class Language(models.Model):
    name = models.CharField(max_length=20)
    native_name = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=5, null=True)

    def __str__(self):
        if self.native_name:
            return f'{self.name}({self.native_name})'
        return f'{self.name}'
