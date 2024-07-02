from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .forms import ProducteForm
from .models import Exemplar, Producte

# Create your views here.
def index(request):
    template= loader.get_template("inventari/index.html")
    return HttpResponse(template.render(request=request))

def llista_productes(request):
    exemplars = None
    if request.method == "POST":
        form = ProducteForm(request.POST)
        if form.is_valid():
            producte = form.cleaned_data['producte']
            exemplars = Exemplar.objects.filter(producte=producte)
    else:
        form = ProducteForm()

    return render(request, 'inventari/inventariProducte.html', {'form': form, 'exemplars': exemplars})

    