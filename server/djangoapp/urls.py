from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
   
    path('yorumlar/', views.yorumlar, name='yorumlar'),
    path('figen_hoca_kimdir/', views.figen_hoca_kimdir, name='figen_hoca_kimdir'),
    path('dersler_hakkinda/', views.dersler_hakkinda, name='dersler_hakkinda'),
    path('iletisim/', views.iletisim, name='iletisim'),
 

    path(route='', view=views.get_feedbacks, name='index'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
