from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)  # Rezervasyonun oluşturulma zamanı
    details = models.TextField(blank=True, null=True)  # İsteğe bağlı açıklama alanı
    restaurant=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"Reservation by {self.name} on {self.date}"
