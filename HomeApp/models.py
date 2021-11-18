from django.db import models

# Create your models here.


class Participant (models.Model):
    nickname = models.CharField(verbose_name='Nickname', max_length=50, blank=False, null=False)
    img = models.ImageField(verbose_name='Image', upload_to='Participants', null=True, blank=True)
    description = models.CharField(verbose_name='Description', max_length=200, blank=True, null=True)
    moty = models.IntegerField(verbose_name='Moty', null=True, default=0)
    poty = models.IntegerField(verbose_name='Poty', null=True, default=0)

    class Meta:
        verbose_name = 'participant'
        verbose_name_plural = 'participants'

    def __str__(self):
        return self.nickname