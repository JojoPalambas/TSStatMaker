from django.http import HttpResponse


def dashboard(request):
    print(request)

    return HttpResponse("Hello, world.")
