from django.db import models

# Create your models here.

class Signature( models.Model ):
    name = models.CharField( max_length=50 )
    surname = models.CharField( max_length=50 )

    time = models.DateTimeField( 'Date Signed' )

    IP = models.CharField( max_length=100 )
    useragent = models.CharField( max_length=250 )



