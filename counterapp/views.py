from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# def root(request):
#     return HttpResponse("Hello World!")
#--------------------------------------------
# def index(request):
#     context = {
#         "time": strftime("%B-%d-%Y %H:%M %p", gmtime())
#     }
#     return render(request, "index.html", context)

def index(request):
    if 'visitcount' in request.session:
        request.session['visitcount'] += 1
    else:
        request.session['visitcount'] = 1
    return render(request, "index.html")

def reset(request):
    del request.session['visitcount']
    return redirect('/')


# def survey(request):
#     # THE INFORMATION COLLECTED FROM THE FORM IS AVAILABLE and represented by THE KEYWORD REQUEST.POST
#     print(request.POST)
#     context = {  # only used to pass info to html
#         'forminfo': request.POST
#     }
#     # return redirect()
#     return render(request, "survey_info.html", context)


# def root(request):
#     return HttpResponse("Hello World!")





