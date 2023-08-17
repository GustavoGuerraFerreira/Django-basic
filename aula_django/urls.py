from django.contrib import admin
from django.urls import path, include
from index import views
urlpatterns = [
    path('',include('index.urls')),
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls'))
]
