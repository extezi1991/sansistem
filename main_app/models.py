from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=64)
    phone=models.CharField(max_length=104)
    message=models.TextField(max_length=1024)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'

