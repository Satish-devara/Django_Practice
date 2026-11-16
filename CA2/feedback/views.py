from django.shortcuts import render,redirect
from .forms import FeedBackForm


def feedback(request):
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('thanks')
    else:
        form = FeedBackForm()
    
    return render(request, 'form.html', {'form' : form})

def thanks(request):
    return render(request, 'thanks.html')




# Create your views here.
