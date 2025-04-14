from django.shortcuts import render,redirect
from base_app.models import Items, ItemList, Feedback, BookTable
from .forms import FeedbackForm, BookTableForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



class CustomLoginView(LoginView):
    template_name = 'login.html'



# Create your views here.
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        return Response({'message': 'This is a protected view! You are authenticated.'})
    
@login_required
def HomeView(request):
    items = Items.objects.all() 
    list = ItemList.objects.all()  
    review = Feedback.objects.all()
    return render(request, 'home.html', {'items': items, 'list': list, 'review': review })



def AboutView(request):
    return  render(request, 'about.html')


def MenuView(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    return render(request, 'menu.html', {'items':items, 'list':list})


@login_required    
def BookTableView(request):
    if request.method=="POST":
        form=BookTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Book_Table')
        else:
            print(form.errors)
    else:
        form=BookTableForm()
    
    return render(request, 'book_table.html',{ 'form':form})


def FeedbackView(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Feedback')  
        else:
            print(form.errors)
    else:
        form = FeedbackForm()
    
    feedback = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedback': feedback, 'form': form})
    