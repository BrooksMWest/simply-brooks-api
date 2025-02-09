from django.conf.urls import include
from rest_framework import routers
from simplybrooksapi.views import BookView
from simplybrooksapi.views import AuthorView
from simplybrooksapi.views import GenreView
from simplybrooksapi.views import BookGenreView
from django.urls import path
from django.contrib import admin
from django.contrib import admin
from django.urls import path

"""simplybrooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'genres', GenreView, 'genre')
router.register(r'books', BookView, 'book')
router.register(r'authors', AuthorView, 'author')
router.register(r'bookGenres', BookGenreView, 'bookGenre' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
