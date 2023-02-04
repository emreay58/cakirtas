from django.shortcuts import render
from .models import Proje, Category, FormModel

# Create your views here.

def IndexView(request):
        if request.method == 'POST':
            message = request.POST['message']
            name = request.POST['name']
            telefon = request.POST['telefon']
            email = request.POST['email']
            subject = request.POST['subject']

            mesaj = FormModel(message=message, name=name, telefon=telefon, email=email,subject=subject)
            mesaj.save()

            return render(request, 'pages/message.html', {'kayit' : 'Mesajınız başarılı bir şekilde oluşturuldu. Sizinle irtibata geçeceğiz.'})
            
        proje = Proje.objects.all()
        category = Category.objects.all()

        context = {
        'proje' : proje,
        'category' : category
    }

        return render(request, 'pages/index.html', context)


def AboutView(request):
    category = Category.objects.all()

    context = {
        'category' : category
    }

    return render(request, 'pages/about.html', context)


def ContactView(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        telefon = request.POST['telefon']
        email = request.POST['email']
        subject = request.POST['subject']

        mesaj = FormModel(message=message, name=name, telefon=telefon, email=email,subject=subject)
        mesaj.save()

        return render(request, 'pages/contact.html', {'kayit' : 'Mesajınız başarılı bir şekilde oluşturuldu. Sizinle irtibata geçeceğiz.'})

    category = Category.objects.all()

    context = {
        'category' : category
    }

    return render(request, 'pages/contact.html', context)


def ProjeView(request):
    proje = Proje.objects.all()
    category = Category.objects.all()

    context = {
         'proje' : proje,
         'category' : category
    }

    return render(request, 'pages/proje.html', context)


def ProjeDetail(request,slug):
    proje = Proje.objects.get(slug=slug)
    category = Category.objects.all()

    context = {
        'proje' : proje,
        'category' : category
    }

    return render(request, 'pages/proje_detail.html', context)


def marka_by_category(request, slug):
    proje = Proje.objects.filter(category__slug=slug)
    category = Category.objects.all()
   
    context = {
        'proje' : proje,
        'category' : category
    }
    return render(request, 'pages/proje.html', context)




