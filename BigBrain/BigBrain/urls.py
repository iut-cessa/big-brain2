from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', include('players.urls')),
    path('questions/', include('questions.urls')),
    path('scoreboard/', include('scoreboard.urls')),
]
