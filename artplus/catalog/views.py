from django.http import HttpResponse
from django.shortcuts import render
from .forms import FeedbackForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template



def about_us(request):
    return render(request,'catalog/about_us.html')




def main(request):
    return render(request,'catalog/main.html')




def catalog(request):
    return render(request,'catalog/catalog.html')

def square(request):
    return render(request,'catalog/square.html')

def figur(request):
    return render(request,'catalog/figur.html')

def besser(request):
    return render(request,'catalog/besser.html')

def borts(request):
    return render(request,'catalog/borts.html')




def contacts(request):
    context = {}
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'],form.cleaned_data['number'])
            context = {'success' : 1}
    else:
        form = FeedbackForm()
    context['form'] = form
    return render(request, 'catalog/contacts.html', context=context)

def send_message(name,number):
    text = get_template('catalog/message.html')
    html = get_template('catalog/message.html')
    context = {'name' : name,'number' : number}
    subject = 'Обратный звонок'
    from_mail = 'defender@gmail.ru'
    text_content = text.render(context)
    html_content = html.render(context)
    
    msg = EmailMultiAlternatives(subject,text_content,from_mail,['hillgary2301@gmail.ru'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()




def feedback(request):
    return render(request, "catalog/feedback.html")
    