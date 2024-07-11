from django.shortcuts import render
from .forms import SimpleForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'formapp/success.html')
        
    else:
        form = SimpleForm()
    return render(request,'formapp/contact.html',{'form':form})