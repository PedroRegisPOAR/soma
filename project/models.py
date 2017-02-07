from django.db import models

# Create your models here.

class ProjeçãoPopulacional(models.Model):
	imagem = models.FileField()

	def delete(self, *args, **kwargs):
		self.imagem.delete()
		super(ProjeçãoPopulacional, self).delete(*args, **kwargs)