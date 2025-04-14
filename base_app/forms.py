from django import forms
from .models import Feedback, BookTable

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user_name', 'description', 'rating', 'image']  
        
        
class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = ['name', 'phone_number', 'email', 'total_person', 'booking_date']