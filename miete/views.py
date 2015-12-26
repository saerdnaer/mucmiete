from django.shortcuts import render, render_to_response

from ipware.ip import get_ip

from .forms import MieteFormPlicht
from .models import Email, Miete

from formtools.wizard.views import SessionWizardView

def index_view(request, **kwargs):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MieteFormPlicht(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = form.save(commit=False)
            obj.ipaddress = get_ip(request)
            obj.save()
            # redirect to a new URL:
            return render(request, 'thanks.html')
    else:
        form = MieteFormPlicht()
        
    # TODO: store both lists in the database
    stadtbezirke   = ['Allach', 'Altstadt', 'Am Hart', 'Au', 'Aubing', 'Berg am Laim', 'Bogenhausen', 'Feldmoching', 'Forstenried', 'Freimann', 'Fürstenried', 'Hadern', 'Haidhausen', 'Harlaching', 'Hasenbergl', 'Isarvorstadt', 'Laim', 'Langwied', 'Lehel', 'Lochhausen', 'Ludwigsvorstadt', 'Maxvorstadt', 'Milbertshofen', 'Moosach', 'Neuhausen', 'Nymphenburg', 'Obergiesing', 'Obermenzing', 'Obersendling', 'Pasing', 'Perlach', 'Ramersdorf', 'Riem', 'Schwabing', 'Schwabing-West', 'Schwanthalerhöhe', 'Sendling', 'Sendling-Westpark', 'Solln', 'Thalkirchen', 'Trudering', 'Untergiesing', 'Untermenzing']
    postleitzahlen = ["80331", "80333", "80335", "80336", "80337", "80339", "80469", "80538", "80539", "80634", "80636", "80637", "80638", "80639", "80686", "80687", "80689", "80796", "80797", "80798", "80799", "80801", "80802", "80803", "80804", "80805", "80807", "80809", "80933", "80935", "80937", "80939", "80992", "80993", "80995", "80997", "80999", "81241", "81243", "81245", "81247", "81249", "81369", "81371", "81373", "81375", "81377", "81379", "81475", "81476", "81477", "81479", "81539", "81541", "81543", "81545", "81547", "81549", "81667", "81669", "81671", "81673", "81675", "81677", "81679", "81735", "81737", "81739", "81825", "81827", "81829", "81925", "81927", "81929"]
    
    return render(request, 'index.html', {'form': form, 'stadtbezirke': stadtbezirke, 'postleitzahlen': postleitzahlen})


class Umfrage(SessionWizardView):
    """
    Does some magic that allows splitting a model-form into different pages.
    Basically, it makes all ModelForm instances use the same Model object.
    """
    def dispatch(self, request, *args, **kwargs):
        self.instance = Miete()
        return super(Umfrage, self).dispatch(request, *args, **kwargs)

    def get_form_instance(self, step):
        return self.instance
        
    def get_template_names(self):
        templates = ["optional.html", "optional.html"]
        return [templates[int(self.steps.current)]]

    def done(self, form_list, **kwargs):
        self.instance.save()
        return render_to_response('thanks.html')

# TODO
"""
            email = form.cleaned_data['email']
            if email:
                Email.objects.get_or_create(email=email)
"""
