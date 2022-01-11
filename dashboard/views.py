from django.shortcuts import redirect, render
from .forms import DataForm
from .models import Data

# Create your views here.
def index(request):
    if request.method=="POST":
        form=DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predict')
    else:
        form=DataForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/index.html',context)

def predict(request):
    predicted_charge = Data.objects.all()
    context={
        'predicted_charge':predicted_charge
    }

    return render(request,'dashboard/predict.html',context)