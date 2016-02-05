from django.shortcuts import render, render_to_response
from django.conf import settings

from ipware.ip import get_ip

from .models import Miete, Email

from formtools.wizard.views import SessionWizardView

class Umfrage(SessionWizardView):
    """
    Does some magic that allows splitting a model-form into different pages by giving every ModelForm the same instance of the Model
    """
    instance = Miete()
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
        
        if "1-email" in self.request.POST:
            Email.objects.get_or_create(addresse=self.request.POST["1-email"])
        
        # Create some friendly server logs
        self.instance.ipaddress = get_ip(self.request)
        self.instance.save()
        print("A Record has been saved: " + str(self.instance.__dict__))
    
    def render(self, form=None, **kwargs):
        if int(self.steps.current) > 0:
            self.save_model()
        
        form = form or self.get_form()
        
        context = self.get_context_data(form=form, **kwargs)
        
        context["stadtbezirke"]   = settings.BEZIRKSTEILE
        context["postleitzahlen"] = settings.PLZ
        context["mapping"]        = settings.PLZ_MAPPING
        
        context["is_embedded"] = "embed" in self.request.GET
        
        return render(self.request, self.get_template_names(), context)
    
    def done(self, form_list, **kwargs):
        self.save_model()
        return render(self.request, "done.html", {"is_embedded": "embed" in self.request.GET})
