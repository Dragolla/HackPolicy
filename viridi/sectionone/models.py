from django.db import models

class Post(models.Model):
    post_title = models.charField(max_length = 30)
    post_details = models.charField(max_length = 1000)
