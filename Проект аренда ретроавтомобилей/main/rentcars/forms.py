from django import forms
from django.core.exceptions import ValidationError
from .models import Feedback, UserClient

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','surname','feedback','email']
        labels ={
            'name':'Укажите имя',
            'surname':'Укажите фамилию',
            'feedback':'Оставьте свой отзыв',
            'email':'Укажите свою почту'
        }

class NumberClient(forms.ModelForm):
    class Meta:
        model = UserClient
        fields = ['name','codphone','phone','ClientChoice']
        labels ={
            'name':'Укажите имя',
            'codphone':'Укажите номер телефона'
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise ValidationError('Укажите только цифры номера')
        return phone