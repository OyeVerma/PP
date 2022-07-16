from django.db import models
from .validators import validate_title
from django.utils.text import slugify

from django.contrib.auth.models import User

class Stack(models.Model):
    image_url = models.URLField(default="https://yt3.ggpht.com/a/AATXAJz4KIO1eJuU6U6hW4ZO_r4eRkQLnNOUtMQ2Dw=s900-c-k-c0xffffffff-no-rj-mo", max_length=200)
    title = models.CharField(unique=True, max_length=50, validators=[validate_title])
    slug = models.SlugField(editable=False, unique=True)
    events = models.ManyToManyField("Event", blank=True, related_name='stack_events')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Stack, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.IntegerField(blank=True)
    text = models.TextField(blank=True)

    def getTextAsPara(self):
        textAsList = []
        for line in self.text.splitlines():
            if len(line.strip()) == 0: continue
            if line[0] == '-':
                textAsList.append(f'<p class="marked">{line[1:]}</p>')
            else:
                textAsList.append(f'<p>{line.title()}</p>')
        return textAsList

    def __str__(self):
        return f'{self.text} - {self.user.username}'