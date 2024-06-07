from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from .models import Car, Feedback
from .forms import FeedbackForm, NumberClient

# Create your views here.

class feedbackView(View):
    def get(self,request):
        show_feed = Feedback.objects.all()
        form = FeedbackForm()
        return render(request, 'MKC_RentCars/feedback.html',{'form':form, 'show_feed':show_feed})
    
    def post(self,request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/MKC_RentCars/Reviews/Thanks/')
        return render(request, 'MKC_RentCars/feedback.html',{'form':form})

def ThanksFeedback(request):
    show_feed = Feedback.objects.order_by('-id')
    last_feedback = show_feed[0]
    return render(request,'MKC_RentCars/ThanksFeedback.html', {'show_feed':show_feed, 'last_feedback':last_feedback})



def main(request):
    status = True
    if request.method == 'POST':
        clientform = NumberClient(request.POST)
        if clientform.is_valid():
            print(clientform.cleaned_data)    
            clientform.save()
            status = False
        return render(request, 'MKC_RentCars/main.html',{'clientform':clientform, 'status':status})
    else:
        clientform = NumberClient()
    return render(request, 'MKC_RentCars/main.html',{'clientform':clientform, 'status':status})



def show_car(request, slug_car:str):
    car = get_object_or_404(Car, slug=slug_car)
    status = True
    if request.method == 'POST':
        clientform = NumberClient(request.POST)
        if clientform.is_valid():
            print(clientform.cleaned_data)  
            clientform.save()
            status = False
        return render(request, 'MKC_RentCars/car.html', {'car':car, 'clientform':clientform, 'status':status})
    else:
        clientform = NumberClient()
    return render(request, 'MKC_RentCars/car.html',{'car':car, 'clientform':clientform, 'status':status})


def show_cars(request):
    cars = Car.objects.order_by('make', 'model')
    return render(request, 'MKC_RentCars/cars.html',{'cars':cars})



def about(request):
    return render(request, 'MKC_RentCars/about.html')

def contacts(request):
    return render(request, 'MKC_RentCars/contacts.html')

def redirectmain(request):
    return HttpResponseRedirect('/MKC_RentCars/')
