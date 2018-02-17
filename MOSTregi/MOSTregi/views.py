from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def test(request):
    return render_to_response('shellTest.html')

def form(request):
    return render_to_response('form.html')

#def test(request):
#    return render_to_response('shellTest.html')
