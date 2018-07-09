import os

from django.db import models

from utils.models import Name


def image_path(instance, filename):
    return os.path.join('logs', 'image', instance.author.username, filename)


class Log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', related_name='logs', on_delete=models.CASCADE)

    type = models.CharField(max_length=10)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, upload_to=image_path)

    watch = models.ForeignKey('logs.Watch', related_name='logs', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.type}-{self.created_at}'


class Watch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='watches', on_delete=models.CASCADE)

    piece = models.ForeignKey('logs.Piece', related_name='watches', on_delete=models.CASCADE)
    start = models.PositiveSmallIntegerField(null=True)
    end = models.PositiveSmallIntegerField(null=True)
    etc = models.CharField(max_length=100, null=True)

    def __str__(self):
        num = None
        if self.start is not None and self.end is not None:
            num = f'{self.start}' if self.start == self.end else f'{self.start}-{self.end}'
        else:
            return f'{self.piece} [{self.etc}]'
        if self.etc is None:
            return f'{self.piece} [{num}]'
        return f'{self.piece} [{num}: {self.etc}]'


class Piece(models.Model):
    titles = models.ManyToManyField('utils.Name', blank=False)
    # TODO: add more information

    def __str__(self):
        return Name.get_default_name(self.titles)
