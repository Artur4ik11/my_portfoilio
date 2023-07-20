from django import forms

 


class FeedbackForm(forms.Form):
    number = forms.CharField(max_length=100,
                            min_length=4,
                            label='Введите ваш номер',
                            widget=forms.TextInput(
                            attrs={'placeholder':'Введите ваш номер','class':'form-control'}
                            )
                            )
    name = forms.CharField(label='Введите ваше Имя',
                           widget=forms.TextInput(
                           attrs={'placeholder':'Введите ваше имя','class':'form-control'}))
    

