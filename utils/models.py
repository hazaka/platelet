from django.db import models


class Name(models.Model):
    text = models.CharField(max_length=255)
    language = models.ForeignKey('utils.Language', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text


class Language(models.Model):
    public_name = models.CharField(max_length=20)
    native_name = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=5, null=True)

    def __str__(self):
        if self.native_name:
            return f'{self.public_name}({self.native_name})'
        return f'{self.public_name}'
