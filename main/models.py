from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 255)
    details = models.TextField()
    image = models.ImageField(upload_to="media/", verbose_name="Image")
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


class VideoNews(models.Model):
    title = models.CharField(max_length = 50)
    link = models.CharField(max_length = 255)
    body = models.CharField(max_length = 200)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"


class Human(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    age = models.IntegerField()
    image = models.ImageField(upload_to="media/", verbose_name="Image", null=True, blank=True)
    info = models.TextField()
    
    class Meta:
        verbose_name = "Odam"
        verbose_name_plural = "Odamlar"


class Contact(models.Model):
    f_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 13)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"