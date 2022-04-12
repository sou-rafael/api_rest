from django.db import models

class Books(models.Model):
    title = models.TextField(max_length=200)
    author = models.CharField(max_length=200)
    pub_com = models.CharField(max_length=200)
    descri = models.TextField(max_length=400)
    quant = models.IntegerField()
    reg_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
