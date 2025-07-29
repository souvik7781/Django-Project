from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety
from .forms import ChaiVarietyForm

# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html')