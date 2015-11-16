from django.shortcuts import render
from ipware.ip import get_ip
from .forms import MieteForm

# Create your views here.

def index_view(request, **kwargs):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MieteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = form.save(commit=False)
            obj.ipaddress = get_ip(request)
            obj.save()
            # redirect to a new URL:
            return render(request, 'thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MieteForm()
    return render(request, 'index.html', {'form': form})
