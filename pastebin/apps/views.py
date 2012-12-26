from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404

from pastebin.apps.forms import PasteForm
from pastebin.apps.models import Paste

import basin

def index(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            new_paste = form.save()
            return HttpResponseRedirect(reverse('detail', kwargs={'id' : new_paste.id}))
    else:
        form = PasteForm()

    return render(request, 'paste_submit.html', {'form' : form})

def detail(request, id):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    nid = basin.decode(alphabet, id)

    paste = get_object_or_404(Paste, pk=nid)
    paste.short = basin.encode(alphabet, paste.id)
    
    return render(request, 'paste_detail.html', {'paste' : paste})
