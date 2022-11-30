from django.db import models

# Create your models here.

class Aspirante(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    tipo_documento = models.CharField('Tipo de documento', max_length=100)
    numero_documento = models.CharField('Documento de identidad', unique=True, max_length=100)
    profesion = models.CharField('Profesión', max_length=100)
    ciudad = models.CharField('Ciudad', max_length=100)
    edad = models.IntegerField('Edad',default=0)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'tipo_documento', 'numero_documento', 'profesion','ciudad','edad']

    def __str__(self):
        return f"Aspirante: documento: {self.numero_documento} nombre: {self.nombre} {self.apellido}"

class Cargo(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    descripcion = models.CharField('Apellido', max_length=100)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['nombre', 'descripcion', 'fecha_creacion',]

    def __str__(self):
        return f"Cargo: {self.nombre} nombre: {self.descripcion} descripcion:"

class EstadoAdmision(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    descripcion = models.CharField('Descripcion', max_length=100)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['fecha_creacion',]

    def __str__(self):
        return f"Estado de Admision: {self.nombre} nombre: {self.descripcion} descripcion:"

class EvaluacionAdmision(models.Model):
    fecha = models.DateField('Fecha de evaluación', auto_now_add=True)
    puntos_cv = models.IntegerField('Puntos Hoja de Vida',default=0)
    puntos_experiencias = models.IntegerField('Puntos Hoja de Vida',default=0)
    puntos_postgrados = models.IntegerField('Puntos Postgrados',default=0)
    puntos_certificaciones = models.IntegerField('Puntos Certificaciones',default=0)
    puntos_ingles = models.IntegerField('Puntos Ingles',default=0)
    total_puntos = models.IntegerField('Total Puntos',default=0)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='cargo', null=True)
    aspirante = models.ForeignKey(Aspirante, on_delete=models.CASCADE, related_name='aspirante')
    admision= models.ForeignKey(EstadoAdmision, on_delete=models.CASCADE, related_name='admision')
    
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['puntos_cv', 'puntos_experiencias', 'puntos_postgrados', 'puntos_certificaciones', 'puntos_ingles','total_puntos']

    def __str__(self):
        return f"Evaluación Admision: fecha: {self.fecha} Total de puntos: {self.total_puntos}"