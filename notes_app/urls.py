from django.conf.urls import url
from . import views

app_name='note_app'

urlpatterns = [
    url(r'^$', views.all_notes, name='all notes'),
    # url(r'^(?P<id>\d+)$', views.detail, name='note_detail')
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='note_detail')

]
