from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
  
  
def indextest(request):
    return HttpResponse("Hello, world.TEST")