from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    icon = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Proje(models.Model):
    title = models.CharField(max_length=150, verbose_name="Proje Adı")
    description1 = models.TextField(null=True)
    image = models.ImageField(upload_to='services', verbose_name="Proje Ana Resim", null=True)
    image1 = models.ImageField(upload_to='services', verbose_name="Resim Detay1")
    image2 = models.ImageField(upload_to='services', verbose_name="Resim Detay2")
    image3 = models.ImageField(upload_to='services', verbose_name="Resim Detay3")
    image4 = models.ImageField(upload_to='services', verbose_name="Resim Detay4")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Marka")
    description = RichTextField(null=True, verbose_name="Detay Açıklama") 
    service = models.CharField(max_length=50, verbose_name="Hizmet Alanı")
    adres = models.CharField(max_length=100, verbose_name="Yer Neresi")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/proje/{self.slug}/'


class FormModel(models.Model):
    message = models.TextField(verbose_name='Mesaj', blank=True)
    name = models.CharField(max_length=100, verbose_name='İsim Soyisim', blank=True)
    telefon = models.CharField(max_length=20, verbose_name="Telefon", blank=True)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
    
    

