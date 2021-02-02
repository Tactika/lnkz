from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortenedURL
import zlib

def index(request):
    url = ShortenedURL.objects.latest('id')
    context = {
        url: url,
    }
    return render(request, 'lnkzio/index.html', context)

def shorturl(request):
    data = request.POST
    code = zlib.crc32(str(data['url']).encode())
    fullURL = ShortenedURL(url=data['url'], code=code)
    fullURL.save()

    # Save URL & Code
    return HttpResponseRedirect(reverse('lnkzio:index'))

def forward(request, code):
    pass
