from django.db import models

""" Modelo de tabla de recuperacion """


class recoveryTable(models.Model):
    nombre = models.CharField(max_length=250, null=False, blank=False,unique=True )
    
    class Meta:
        db_table = 'recoveryTable'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre