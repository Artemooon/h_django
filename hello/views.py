from django.http import HttpResponse


def index(request):
    return HttpResponse('<marquee behavior="scroll" direction="right" scrollamount="30">Hello, world.</marquee>')