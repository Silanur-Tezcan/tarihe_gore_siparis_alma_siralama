from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'created_at', 'details', 'restaurant','delete_link')  # Silme bağlantısını ekledik
    ordering = ('created_at',)  # Rezervasyonları oluşturulma zamanına göre sırala
    search_fields = ('name', 'phone')  # Arama yaparken ad ve telefonla arama yapılabilir

    # Silme linki oluşturmak için
    def delete_link(self, obj):
        return f'<a href="/admin/{obj._meta.app_label}/{obj._meta.model_name}/{obj.id}/delete/">Sil</a>'
    delete_link.allow_tags = True  # HTML etiketi kullanarak bağlantıyı doğru biçimde gösterir.
    delete_link.short_description = 'Sil'  # Bu alanın adını "Sil" olarak belirledik
