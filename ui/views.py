from django.shortcuts import render, redirect
from django.contrib.gis.geoip import GeoIP
from django.utils import timezone
from guestbook.settings import CAN_SIGN_AGAIN

from ui.models import Signature

import os

# Relative path to root directory
GEOIP_PATH = os.path.realpath( os.path.join( os.path.dirname( os.path.realpath( __file__ ) ), '..', 'geo' ) )

def index( request ):
    """Main index view with something about myself.
    """
    r = { }
    signatures = Signature.objects.order_by('-time')

    ip = request.META.get( 'REMOTE_ADDR' )
    r['has_signed'] = False
    r['signatures_exist'] = False

    if CAN_SIGN_AGAIN:
        r['sign_again'] = True

    if signatures.count( ) > 0:
        for s in signatures:
            if s.IP == ip: 
                r['has_signed'] =  True
                break

        r['signatures_exist'] = True
        r['signatures'] = signatures

    return render( request, 'ui/index.html', r )

def sign( request ):
    """Signs the main guestbook, takes no options as there's only one guestbook.
    """
    signatures = Signature.objects.order_by('-time')
    ip = request.META.get( 'REMOTE_ADDR' )

    for s in signatures:
        if s.IP == ip: 
            return redirect( index )
    else:
        p = request.POST
        Signature( name=p['name'], surname=p['surname'], IP=ip, time=timezone.now( ) ).save( )

    return redirect( index )

def signatures( request ):
    r = { }
    signatures = Signature.objects.order_by('-time')

    r['signatures_exist'] = False

    if signatures.count( ) > 0:
        for s in signatures:
            g = GeoIP( path=GEOIP_PATH )
            geodata = g.city( s.IP )

            if geodata is not None:
                s.country = ', '.join( [ geodata['city'], geodata['country_code3'] ] )
            else:
                s.country = "Unknown"
            r['signatures_exist'] = True
            r['signatures'] = signatures

    return render( request, 'ui/signatures.html', r )
