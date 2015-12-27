from django.shortcuts import render, render_to_response

from ipware.ip import get_ip

from .models import Miete

from formtools.wizard.views import SessionWizardView

class Umfrage(SessionWizardView):
    instance = Miete()
    """
    Does some magic that allows splitting a model-form into different pages by giving every ModelForm the same instance of the Model
    """
    def dispatch(self, request, *args, **kwargs):
        return super(Umfrage, self).dispatch(request, *args, **kwargs)
        
    def get_form_instance(self, step):
        return self.instance
    
    def get_template_names(self):
        templates = ["index.html", "optional.html"]
        return [templates[int(self.steps.current)]]
    
    def save_model(self):
        """
        Custom method for saving the Model after every step
        """
        # Create some friendly server logs
        self.instance.ipaddress = get_ip(self.request)
        self.instance.save()
        print("A Record has been saved: " + str(self.instance.__dict__))
    
    def render(self, form=None, **kwargs):
        if int(self.steps.current) > 0:
            self.save_model()
            
        form = form or self.get_form()
        context = self.get_context_data(form=form, **kwargs)
        
        # TODO: store both lists in the database
        context["stadtbezirke"]   = ['Allach', 'Altstadt', 'Am Hart', 'Au', 'Aubing', 'Berg am Laim', 'Bogenhausen', 'Feldmoching', 'Forstenried', 'Freimann', 'Fürstenried', 'Hadern', 'Haidhausen', 'Harlaching', 'Hasenbergl', 'Isarvorstadt', 'Laim', 'Langwied', 'Lehel', 'Lochhausen', 'Ludwigsvorstadt', 'Maxvorstadt', 'Milbertshofen', 'Moosach', 'Neuhausen', 'Nymphenburg', 'Obergiesing', 'Obermenzing', 'Obersendling', 'Pasing', 'Perlach', 'Ramersdorf', 'Riem', 'Schwabing', 'Schwabing-West', 'Schwanthalerhöhe', 'Sendling', 'Sendling-Westpark', 'Solln', 'Thalkirchen', 'Trudering', 'Untergiesing', 'Untermenzing']
        context["postleitzahlen"] = ["80331", "80333", "80335", "80336", "80337", "80339", "80469", "80538", "80539", "80634", "80636", "80637", "80638", "80639", "80686", "80687", "80689", "80796", "80797", "80798", "80799", "80801", "80802", "80803", "80804", "80805", "80807", "80809", "80933", "80935", "80937", "80939", "80992", "80993", "80995", "80997", "80999", "81241", "81243", "81245", "81247", "81249", "81369", "81371", "81373", "81375", "81377", "81379", "81475", "81476", "81477", "81479", "81539", "81541", "81543", "81545", "81547", "81549", "81667", "81669", "81671", "81673", "81675", "81677", "81679", "81735", "81737", "81739", "81825", "81827", "81829", "81925", "81927", "81929"]
        
        return render(self.request, self.get_template_names(), context)
    
    def done(self, form_list, **kwargs):
        self.save_model()
        return render_to_response('done.html')

# TODO
"""
            email = form.cleaned_data['email']
            if email:
                Email.objects.get_or_create(email=email)
"""
