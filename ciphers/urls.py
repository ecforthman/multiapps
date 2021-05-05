from django.conf.urls import url

from django.urls import path
from ciphers import views

app_name = 'ciphers'

urlpatterns = [
    path('', views.index, name='ciphers_index'),
    path('encode', views.encode, name='ciphers_encode'),
    url(r'encrypted_doc', views.encrypted_doc, name='ciphers_encrypted_doc'),
    path('list_docs', views.list_docs, name='ciphers_list_docs'),
    path('decode', views.decode, name='ciphers_decode'),
    path('read_message', views.read_message, name='ciphers_read_message'),
]
