Guestbook
=========

Part of the Lumate technical challenge. This Guestbook allows basic signing and then viewing all signatures.

Setup
=====

Please see requirements.txt for packages that need to be installed. Please ensure postgres is properly setup for
your distribution.

Create postgres database guestbook and grant user all rights:
  sudo su postgres                                                                                         
  psql                                                                                                     

  CREATE DATABASE guestbook;                                                                               
  CREATE ROLE |user|;                                                                                      
  GRANT ALL ON DATABASE guestbook TO |user|;                                                               
  ALTER ROLE |user| WITH LOGIN;
  
Enter cloned directory and:                                                     
  python manage.py makemigrations ui                                                                       
  python manage.py sqlmigrate ui 0001                                                                      
  python manage.py runserver 0.0.0.0:8000                                                                  
  python manage.py migrate                                                                                 

Grab Geolite databases including "GeoLite City" and "GeoLite Country" from here:                     
  http://dev.maxmind.com/geoip/legacy/geolite/                                                             

Afterwards, store them in a new folder named geo, extracted (guestbook/geo/).

Finally, change the secret key within guestbook/settings.py.

Settings
========

Most settings are found in guestbook/settings.py. The primary setting which can be used is CAN_SIGN_AGAIN. 
Enabling this allows any user to sign more than once, within any timespan (no timeout). When disabled,
only one signature per IP is allowed.
