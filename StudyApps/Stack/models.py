import json
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from .validators import validate_title
# Create your models here.
class fromCSV(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    file = models.FileField(upload_to='csv/', max_length=100)
    content = models.TextField(blank=True)

    def __str_(self):
        return self.title

    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

class Topic(models.Model):
    image_url = models.URLField(default="https://yt3.ggpht.com/a/AATXAJz4KIO1eJuU6U6hW4ZO_r4eRkQLnNOUtMQ2Dw=s900-c-k-c0xffffffff-no-rj-mo", max_length=200)
    title = models.CharField(unique=True, max_length=50, validators=[validate_title])
    text = models.TextField()
    slug = models.SlugField(editable=False, unique=True)
    topics = models.ManyToManyField("Topic", blank=True)

    def __str__(self):
        return slugify(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

    def getTextList(self):
        d = []
        heads = []
        lines = self.text.split('\n')
        cwlist = []
        for line in lines:
            if line != '':
                if line[:2] == '--':
                    cwlist.append(line[2:])
                elif line[0] == '-':
                    if len(cwlist) != 0:
                        d.append(cwlist)
                        heads.append(line[1:])
                        cwlist = []
                    cwlist.append(line[1:])
        heads.append(line[1:])
        d.append(cwlist)
        return d, heads

class StudyApps(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)