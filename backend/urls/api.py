from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
# from django.contrib import admin

urlpatterns = []
try:
    urlpatterns = urlpatterns + []
except NameError:
    pass

urlpatterns = urlpatterns + [

    url(r'^user/',
        include('users.urls',
            namespace='users')
        ),


]

if settings.DEBUG:

    # allows users to authenticate with the api using the rest framework forms
    urlpatterns.append(
        url(r'^api-auth/',
            include('rest_framework.urls',
                namespace='rest_framework')
        ))

