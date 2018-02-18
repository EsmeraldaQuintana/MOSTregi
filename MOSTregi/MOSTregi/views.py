from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def form(request):
    return render_to_response('form.html')

def confirm(request):
    return render_to_response('confirm.html')

def home(request):
    return render_to_response('home.html')

def exhibitions(request):
    return render_to_response('exhibitions.html')

def collections(request):
    return render_to_response('collections.html')
#def test(request):
#    return render_to_response('shellTest.html')
