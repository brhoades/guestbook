from django.conf.urls import url

from ui import views

urlpatterns = [ url( r'^$', views.index, name='index' ),
                url( r'^sign$', views.sign, name='sign' ) ]
