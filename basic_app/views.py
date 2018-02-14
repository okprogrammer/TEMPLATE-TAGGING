from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'name':'Hello world','number':100}
    return render(request,'basic_app/index.html',context=my_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')