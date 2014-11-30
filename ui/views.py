from django.shortcuts import render

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

