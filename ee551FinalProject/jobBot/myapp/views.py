from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import searchForm
from .models import searchData

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            form.process()
            return HttpResponseRedirect('/thanks/')
    else:
        form = searchForm()
        
    return render(request, 'myapp/index.html', {'form': form})

def thanks(request):
    return HttpResponse("thank you for your submission")

def saved(request):
    return HttpResponse("see saved seaches")
