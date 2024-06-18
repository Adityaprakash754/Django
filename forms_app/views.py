from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.
def contact_us(request):
    # u have to handle form submission
    if request.method == 'POST':
        # check if the form is valid if not render it again with the same contents along with error
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Alright no errors!")
    else:
        form = ContactForm()

    return render(request, 'contactUs.html', {'form': form})
