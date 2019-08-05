# Complete Reususable Comments 



[![CircleCI](https://circleci.com/gh/NYARAS/Resuseable-Comments-CI.svg?style=svg)](https://circleci.com/gh/NYARAS/Resuseable-Comments-CI)

Calvine Comments
A reusable Django & Javascript app (jQuery) for simply implementing a comments feed on any url.

Quick start
Install Calvine Comments & Dependancies:

pip install django-calvo-comments django djangorestframework django-cors-headers
Add "comments" to your INSTALLED_APPS setting like this:

INSTALLED_APPS = [
    ...
    'corsheaders', 
    'rest_framework',
    'comments',
]
Implement Django Dependancy Settings:

Django Rest Framework
Django Cors Headers
Such as:

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}



CORS_URLS_REGEX = r'^/api.*'
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*',
)

Add the following to ROOT_URLCONF:

from django.conf.urls import url, include
urlpatterns = [
    ...
    url(r'^api/comments/', include('comments.api.urls')),
]
Add jQuery and Bootstrap(recommended):

<!-- jQuery Required -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

<!-- Bootstrap JS Recommeded -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<!-- Bootstrap CSS Recommeded -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
Add Srvup.Comments.js:

{% load static %} 

<!-- Primary Static files -->
<script src='{% static "comments/js/srvup.comments.js" %}'></script>

<!-- CSRF Safe For Ajax -->
<script src='{% static "comments/js/srvup.safeajax.js" %}'></script>
Run Django Commands:

python manage.py makemigrations

python manage.py migrate
Use!

<div class='srvup-load-comments' data-url='{{ request.build_absolute_uri }}'></div>
Customize:

<div class='srvup-load-comments' data-url='/any/path/' data-login='/accounts/login/' data-api-endpoint='/api/comments/'></div>
data-url: Any url path you want your comments to load for that path