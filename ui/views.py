from django.http import HttpResponse
from ui.models import Signature

def index( request ):
    """Main index view with something about myself.
    """
    r = [ ]
    signatures = Signature.objects

    if signatures.count( ) == 0:
        r.append( "Nobody has signed my guestbook yet." )
    else:
        for s in signatures:
            r.append( ''.join( s.surname, ", ", s.name ) )
            
    # Add form?
    return HttpResponse( '\n'.join( r ) )

