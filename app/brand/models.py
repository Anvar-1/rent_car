from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand/', null=True, blank=True)
    # price = models.DecimalField(max_digits=20, decimal_places=2)


    def __str__(self):
        return f'id{self.id}: {self.name}'

    


