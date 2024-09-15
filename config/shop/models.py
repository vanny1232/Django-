from django.db import models

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"({self.id}) {self.name}"

class product(models.Model):
    name = models.CharField(max_length=255)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    price = models.FloatField()
    valume = models.CharField(max_length=10)
    disciptions = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/')
    def __str__(self):
        return f"{self.id}.{self.name}"

