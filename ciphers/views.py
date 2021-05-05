from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.utils import timezone

from ciphers.models import SavedDocs
from ciphers.forms import CipherTextForm
from ciphers.cipherlib import encrypt_file, encrypt_word, decrypt_file
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

def index(request):
    return render(request, 'ciphers_index.html')


# pass  # does nothing, just trigger the validation
# return HttpResponseRedirect('cipher/encrypted_doc.html', {'form': form})
# print(form.data) shows dictionary
# print(form['text'].value())
# print (form.cleaned_data['title'])
# print (form.cleaned_data['author'])
# print (form.cleaned_data['text'])
# print (form.cleaned_data)

def encode(request):
    if request.method == 'POST':
        form = CipherTextForm(request.POST)
        if form.is_valid():
            create_record(form.cleaned_data)
            #title = form.cleaned_data['title']
            offset = form.cleaned_data['cipher_key_offset']
            key = encrypt_word(form.cleaned_data['cipher_key'], int(offset))
            return encrypted_success({'key': key, 'offset': offset})
    else:
        form = CipherTextForm()
    return render(request, 'ciphers_encode.html', {'form': form})


def encrypted_doc(request):
    return render(request, 'ciphers_encrypted_doc.html' )


def encrypted_success(dict_in):
    #din = dict_in.copy()
    key = dict_in.get('key')
    offset = dict_in.get('offset')
    return redirect(f"ciphers_encrypted_doc.html?key={key}&offset={offset}")

def list_docs(request):
    encrypted_docs = SavedDocs.objects.all()
    context = {'encrypted_docs': encrypted_docs}
    return render(request, 'ciphers_list_docs.html', context)


def decode(request):
    if request.method == 'POST':
        rec_id = request.POST.get('record_number')
        message = SavedDocs.objects.get(pk=rec_id)
        data = {'title' : message.title, 'author': message.author,
                'text': message.encrypted_text}
        form = CipherTextForm(initial=data)
        return render(request, 'ciphers_decode.html', {'form': form})


#@csrf_protect
def read_message(request):
    cipherKey = request.POST.get('cipher_key')
    cipherKeyOffset = request.POST.get('cipher_key_offset')
    encryptedMessageText = request.POST.get('text')
    post_pass = decrypt_file(encryptedMessageText, cipherKey, int(cipherKeyOffset))
    context = {'post_pass': post_pass}
    return render(request, 'ciphers_read_message.html', context)



# ----- database functions ----------------

def create_record(recDict):
    new_record = SavedDocs(title=recDict['title'],
                           author=recDict['author'],
                           date_submitted=timezone.now(),
                           encrypted_text=encrypt_file(recDict['text'],
                                                       recDict['cipher_key'],
                                                       int(recDict['cipher_key_offset'])))
    new_record.save()