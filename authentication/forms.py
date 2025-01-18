from django import forms
from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    username=forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class":"form-control"}))
    date_of_birth=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "type":"date"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password_confirmation=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = CustomUser
        fields=["username", "email", "date_of_birth", "location", "password", "password_confirmation"]


    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get("password")
        password_confirmation=cleaned_data.get("password_confirmation")
        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Password and confirmation password do not match")
        else:
            return cleaned_data
        
