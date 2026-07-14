from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    data = models.JSONField(default=dict, verbose_name="Ma'lumotlar")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ma\'lumot'
        verbose_name_plural = 'Ma\'lumotlar'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"