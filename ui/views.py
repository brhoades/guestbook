from django.shortcuts import render
from django.utils import timezone

from ui.models import Signature

def index( request ):
    """Main index view with something about myself.
    """
    r = { }
    signatures = Signature.objects

    if signatures.count( ) > 0:
        r['signatures_exist'] = True
        r['signatures'] = signatures.order_by('-time')

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
    p = request.POST
    Signature( name=p['name'], surname=p['surname'], IP="0.0.0.0", time=timezone.now( ) ).save( )

    return index( request )

