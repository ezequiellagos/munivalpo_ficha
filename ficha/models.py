from django.db import models

REGION_CHOICES = [
    ('VALPARAÍSO', 'Valparaíso'),
]

COMUNA_CHOICES = [
    ('VALPARAÍSO', 'Valparaíso'),
    ('LAGUNA VERDE', 'Laguna Verde'),
    ('PLACILLA', 'Placilla'),
    ('PLAYA ANCHA', 'Playa Ancha'),
]

# Sección 1
class IdentificacionInmueble(models.Model):
    id_plano = models.BigAutoField(primary_key=True)
    rol = models.CharField(max_length=100, blank=True, default='')
    unidad_vecinal = models.CharField(max_length=255, blank=True, default='')
    region = models.CharField(max_length=50, choices=REGION_CHOICES, default='VALPARAÍSO')
    comuna = models.CharField(max_length=50, choices=COMUNA_CHOICES, default='VALPARAÍSO')
    calle = models.CharField(max_length=255, blank=True, default='')
    numero = models.CharField(max_length=50, blank=True, default='')
    plan_cerro_poblacion = models.CharField(max_length=255, blank=True, default='')
    denominacion_inmueble = models.CharField(max_length=255, blank=True, default='')
    autor = models.CharField(max_length=255, blank=True, default='Se desconoce')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "identificacion_inmueble"
        verbose_name_plural = "identificaciones_inmuebles"

    def __str__(self):
        return str(self.id_plano) + ' - ' + self.rol

# Sección 2
class PlanoUbicacion(models.Model):
    imagen_plano = models.ImageField(upload_to="plano_ubicacion")
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "plano_ubicacion"
        verbose_name_plural = "planos_ubicaciones"

# Sección 3
class FotografiaGeneral(models.Model):
    imagen_fotografia = models.ImageField(upload_to="fotografia_general")
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "fotografia_general"
        verbose_name_plural = "fotografias_generales"

# Sección 4
class FotografiaContexto(models.Model):
    registro_fotografico_1 = models.ImageField(upload_to="fotografia_contexto")
    registro_fotografico_2 = models.ImageField(upload_to="fotografia_contexto")
    fecha_registro_fotografico = models.DateField()
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "fotografia_contexto"
        verbose_name_plural = "fotografias_contextos"

# Sección 5
class ResenaPatrimonial(models.Model):
    valor_urbano = models.TextField()
    valor_arquitecnico = models.TextField()
    valor_historico = models.TextField()
    valor_economico_social = models.TextField()
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "resena_patrimonial"
        verbose_name_plural = "resenas_patrimoniales"

# Sección 6
class ValoracionAtributos(models.Model):
    valor_urbano_a = models.PositiveSmallIntegerField(default=0)
    valor_urbano_b = models.PositiveSmallIntegerField(default=0)
    valor_urbano_c = models.PositiveSmallIntegerField(default=0)

    valor_arquitecnico_a = models.PositiveSmallIntegerField(default=0)
    valor_arquitecnico_b = models.PositiveSmallIntegerField(default=0)
    valor_arquitecnico_c = models.PositiveSmallIntegerField(default=0)

    valor_historico_a = models.PositiveSmallIntegerField(default=0)
    valor_historico_b = models.PositiveSmallIntegerField(default=0)

    valor_economico_social_a = models.PositiveSmallIntegerField(default=0)
    valor_economico_social_b = models.PositiveSmallIntegerField(default=0)
    valor_economico_social_c = models.PositiveSmallIntegerField(default=0)

    zona_de_conservacion = models.CharField(max_length=255)
    identificacion_zch = models.CharField(max_length=100)
    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "valoracion_atributos"
        verbose_name_plural = "valoraciones_atributos"

# Sección 7
PERIODOS_CONSTRUCCION = [
    ('ANTERIOR A 1900', 'Anterior a 1900'),
    ('1901-1920', '1901-1920'),
    ('1921-1940', '1921-1940'),
    ('1941-1960', '1941-1960'),
    ('1961-1970', '1961-1970'),
    ('1971-1990', '1971-1990'),
    ('POST 1990', 'Post 1990'),
]

TIPO_PROPIEDAD = [
    ('PARTICULAR', 'Particular'),
    ('FISCAL', 'Fiscal'),
    ('MUNICIPAL', 'Municipal'),
]

TIPO_USUARIO = [
    ('PROPIETARIO', 'Propietario'),
    ('ARRENDATARIO', 'Arrendatario'),
    ('USUFRUCTUARIO', 'Usufructuario'),
]

REGIMEN_PROPIEDAD = [
    ('INDIVIDUAL', [
        ('PERSONA NATURAL', 'Persona Natural'),
        ('PERSONA JURIDICA', 'Persona Jurídica'),
    ]),
    ('COLECTIVA', [
        ('COMUNIDAD', 'Comunidad'),
        ('SUCESION', 'Sucesión'),
    ]),
]

AFECTACION_ACTUAL = [
    ('DECLARACION DE UTILIDAD PUBLICA', 'Declaración de Utilidad Pública'),
    ('ANTEJARDIN', 'Antejardín'),
    ('OTRO', 'Otro'),
]

class InformacionTecnica(models.Model):
    piso_original_subterraneo = models.CharField(max_length=255, blank=True, default='')
    piso_original_primer_piso = models.CharField(max_length=255, blank=True, default='')
    piso_original_pisos_superiores = models.CharField(max_length=255, blank=True, default='')
    piso_actual_subterraneo = models.CharField(max_length=255, blank=True, default='')
    piso_actual_primer_piso = models.CharField(max_length=255, blank=True, default='')
    piso_actual_pisos_superiores = models.CharField(max_length=255, blank=True, default='')

    anio_construccion = models.CharField(max_length=50, choices=PERIODOS_CONSTRUCCION, default='ANTERIOR A 1900')

    tipo_propiedad = models.CharField(max_length=50, choices=TIPO_PROPIEDAD, default='PARTICULAR')
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO, default='PROPIETARIO')

    regimen_propiedad = models.CharField(max_length=50, choices=REGIMEN_PROPIEDAD, default='INDIVIDUAL')

    afectacion_actual = models.CharField(max_length=50, choices=AFECTACION_ACTUAL, default='DECLARACION DE UTILIDAD PUBLICA')

    observaciones = models.TextField(blank=True, default='')

    id_plano = models.OneToOneField(IdentificacionInmueble, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "informacion_tecnica"
        verbose_name_plural = "informaciones_tecnicas"

# Sección 8
TIPOLOGIA = [
    
]
# class CaracteristicasMorfologicas(models.Model):
    


