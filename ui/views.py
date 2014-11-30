from django.shortcuts import render
from time import time

from ui.models import Signature

def index( request ):
    """Main index view with something about myself.
    """
    r = { }
    signatures = Signature.objects

    if signatures.count( ) == 0:
        r['there_are_no_signatures'] = True
    else:
        r['signatures'] = signatures

    return render( request, 'ui/index.html', r )

def sign( request ):
    """Signs the main guestbook, takes no options as there's only one guestbook.
    """
    # Have they signed within TIMEOUT to prevent blatent abuse
    #ip = request.META.get( 'REMOTE_ADDR' )

    #for s in Signature.objects:
    #    if s.IP == ip and s.time + 60 > time.time( ): 
    #        r = { 'name': request.POST['name'],
    #              'surname': request.POST['surname'] }
    #        return render( request, 'ui/index.html', r )
    #else:
    return index( request )

