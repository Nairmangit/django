from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30 ,'placeholder':'Введите что вы хотите сделать','autocomplete':'off'}))