from django.shortcuts import render
from .forms import MessageForm

# Create your views here.
def send_message(request):
    form=MessageForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])
        print(data["phone"])

        new_form = form.save()
    return render(request, 'landing.html', locals())
