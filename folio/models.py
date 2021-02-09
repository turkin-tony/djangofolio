#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Project(models.Model):

    TYPE_BLOCK = (
        ('400', '400px'),
        ('600', '600px'),
    )

    project_name = models.CharField(max_length = 100, verbose_name=u'имя')
    project_slug = models.SlugField(max_length = 100, verbose_name=u'Чпу')
    project_poster = models.ImageField(verbose_name=u'Изображение',
                                      upload_to='media/%Y/%m/%d',
                                      blank=True, null=True)
    project_pub = models.DateTimeField(auto_now_add=True)
    project_text = models.TextField(max_length=1000, verbose_name=u'Текст')
    project_type_block = models.CharField(max_length=3,
                                          verbose_name=u'Ширина блока',
                                          choices=TYPE_BLOCK)

    class Meta:
        db_table = 'projects'
        verbose_name = u'Проект'
        verbose_name_plural = u'Проекты'

    def __unicode__(self):
        return self.project_name

    def get_image(self):
        return "/media/%s" % self.project_poster


class ProjectTags(models.Model):
    project_tag = models.CharField(max_length = 100, verbose_name=u'Метка')
    project = models.ForeignKey(Project)

    class Meta:
        db_table = 'projects_tags'
        verbose_name = u'Метка'
        verbose_name_plural = u'Метки'

    def __unicode__(self):
        return self.project_tag


class ProjectGallery(models.Model):
    project_image = models.ImageField(verbose_name=u'Изображение',
                                      upload_to='media/%Y/%m/%d',
                                      blank=True, null=True)
    project = models.ForeignKey(Project)

    class Meta:
        db_table = 'projects_gallery'
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения'


    def get_image(self):
        return "/media/%s" % self.project_image
