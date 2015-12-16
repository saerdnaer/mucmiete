from django.shortcuts import render
from ipware.ip import get_ip
from .forms import MieteForm
from .models import Email

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
            email = form.cleaned_data['email']
            if email:
                Email.objects.get_or_create(email=email)
            # redirect to a new URL:
            return render(request, 'thanks.html')
    
    # if a GET (or any other method) we'll create a blank form
    form = MieteForm()
    
    # TODO: store both lists in the database
    stadtteile   = ["Allach", "Untermenzing", "Altstadt", "Lehel", "Au", "Haidhausen", "Aubing", "Lochhausen", "Langwied", "Berg am Laim", "Bogenhausen", "Feldmoching", "Hasenbergl", "Hadern", "Laim", "Ludwigsvorstadt", "Isarvorstadt", "Maxvorstadt", "Milbertshofen", "Am Hart", "Moosach", "Neuhausen", "Nymphenburg", "Obergiesing", "Pasing", "Obermenzing", "Ramersdorf", "Perlach", "Schwabing", "Freimann", "Schwabing-West", "Schwanthalerhöhe", "Sendling", "Sendling-Westpark", "Thalkirchen", "Obersendling", "Fürstenried", "Forstenried", "Solln", "Trudering", "Riem", "Untergiesing", "Harlaching"]
    postleitzahl = ["80331", "80333", "80335", "80336", "80337", "80339", "80469", "80538", "80539", "80634", "80636", "80637", "80638", "80639", "80686", "80687", "80689", "80796", "80797", "80798", "80799", "80801", "80802", "80803", "80804", "80805", "80807", "80809", "80933", "80935", "80937", "80939", "80992", "80993", "80995", "80997", "80999", "81241", "81243", "81245", "81247", "81249", "81369", "81371", "81373", "81375", "81377", "81379", "81475", "81476", "81477", "81479", "81539", "81541", "81543", "81545", "81547", "81549", "81667", "81669", "81671", "81673", "81675", "81677", "81679", "81735", "81737", "81739", "81825", "81827", "81829", "81925", "81927", "81929"]
    
    return render(request, 'index.html', {'form': form, 'stadtteile': stadtteile, 'postleitzahl': postleitzahl})
