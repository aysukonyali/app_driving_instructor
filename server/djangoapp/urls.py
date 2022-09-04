from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for yourmlar  view
    path('yorumlar/', views.yorumlar, name='yorumlar'),
    path('figen_hoca_kimdir/', views.figen_hoca_kimdir, name='figen_hoca_kimdir'),
    path('dersler_hakkinda/', views.dersler_hakkinda, name='dersler_hakkinda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_feedbacks, name='index'),
    #path('add_review/', views.add_feedback, name='add_review'),

    # path for dealer reviews view

    # path for add a review view


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)