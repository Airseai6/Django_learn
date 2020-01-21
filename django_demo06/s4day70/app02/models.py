from django.db import models

# Create your models here.
class Boy(models.Model):
    name = models.CharField(max_length=32)
    # m = models.ManyToManyField('Girl', through='Love', through_fields=('b','g',))


class Girl(models.Model):
    nick = models.CharField(max_length=32)
    # m = models.ManyToManyField('Boy')


class Love(models.Model):
    b = models.ForeignKey('Boy', on_delete=models.CASCADE, )
    g = models.ForeignKey('Girl', on_delete=models.CASCADE, )

    class Meta:
        unique_together = [
            ('b', 'g'),
        ]


class UserAdmin(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)




