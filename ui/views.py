from django.http import HttpResponse

def index( request ):
    """Main index view with something about myself.
    """
    return HttpResponse( "This is a page about me." )

