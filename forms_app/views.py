from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contactUs (request):
    form = ContactForm()
    return render(request,'contactUs.html', {'form': form})
