from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='movies/', null=True, blank=True)  # 👈 NUEVO
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title