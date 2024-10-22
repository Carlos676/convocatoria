from django.db import models

# Create your models here.
class Departamento(models.Model):
    departamento = models.CharField(max_length=50,verbose_name= ("Ingrese Departamentos"),null=False,blank=False)
    def __str__(self):
        return "%s" % (self.departamento)
    
    
    
class Responsable_proyecto(models.Model):
    nombre = models.CharField(
        max_length=50,
        verbose_name= ("Nombre Completo:"),
        null=False,
        blank=False
    )
    
    cargo_proyecto = models.TextField(
        verbose_name=("Cargo de Proyecto"),
        null=False, blank=False,
    )
    
    celular = models.IntegerField(
        verbose_name=("Cargo de Proyecto"),
        null=False, blank=False,
    )
    
    correo = models.CharField(
        verbose_name=("Correo Electronico"),
        max_length=50,
        null=False, blank=False,
    )