from django.db import models

class Paste(models.Model):

    code = 	models.TextField()
    title = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add = True)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Paste'
        verbose_name_plural = 'Pastes'

    def __unicode__(self):
        return self.title
