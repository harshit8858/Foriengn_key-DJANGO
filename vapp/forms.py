from django import forms
from .models import *


class Publisherform(forms.ModelForm):
    def clean_email(self):
        mail = self.cleaned_data['email']

        try:
            match = Publisher.objects.get(email__iexact=mail)
        except:
            return mail
        raise forms.ValidationError("already exists.")

    def clean_pubname(self):
        pname = self.cleaned_data['pubname']

        try:
            match = Publisher.objects.get(pubname__iexact = pname)
        except:
            return pname
        raise forms.ValidationError('already there!!')

    class Meta:
        model = Publisher
        fields = '__all__'


class Bookform(forms.ModelForm):

    #publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())
    #above line is req. if specicfic fields are considered..

    def clean_title(self):
        t = self.cleaned_data['title']

        try:
            book_name = Book.objects.get(title__iexact=t)
        except Book.DoesNotExist:
            return self.cleaned_data['title']
        raise forms.ValidationError("This book already exists.")

    class Meta:
        model = Book
        fields = '__all__'
        # fields='__all__'  #if all field is considered then ModelChoiceField wali line is not req.

class Postform(forms.ModelForm):
    class Meta:
        models = Publisher
        fields = ['title','content']