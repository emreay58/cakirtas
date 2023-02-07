from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    icon = models.CharField(max_length=100, null=True, verbose_name="İcon Kodu")
    name = models.CharField(max_length=50, verbose_name="Faaliyet Alanı Ekle" )
    description = models.TextField(null=True, verbose_name="Faaliyet Alanı Açıklama")
    slug = models.SlugField(null=True, blank=True, verbose_name="Bu kısım otomatik dolmaktadır.")

    def __str__(self):
        return self.name
    

class Proje(models.Model):
    title = models.CharField(max_length=150, verbose_name="Proje Adı")
    description1 = models.TextField(null=True, verbose_name="Ana Sayfa Başlığı")
    seotitle = models.TextField(null=True, max_length=70, verbose_name="Seo Başlığı")
    seodescription = models.CharField(max_length=170, verbose_name="Seo Açıklama Kısmı")
    image = models.ImageField(upload_to='services', verbose_name="Proje Ana Resim", null=True)
    image1 = models.ImageField(upload_to='services', verbose_name="Resim Detay1")
    image2 = models.ImageField(upload_to='services', verbose_name="Resim Detay2")
    image3 = models.ImageField(upload_to='services', verbose_name="Resim Detay3")
    image4 = models.ImageField(upload_to='services', verbose_name="Resim Detay4")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Faaliyet Alanı")
    description = RichTextField(null=True, verbose_name="İşletme Açıklama") 
    service = models.CharField(max_length=50, verbose_name="Hizmet Alanı")
    adres = models.CharField(max_length=100, verbose_name="Yer Neresi")
    date = models.DateField(auto_now=True, verbose_name="Proje Ekleme Tarihi")
    is_home= models.BooleanField(verbose_name="Ana Sayfada Gösterilsin Mi", default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/proje/{self.slug}/'


class FormModel(models.Model):
    message = models.TextField(verbose_name='Mesaj', blank=True)
    name = models.CharField(max_length=100, verbose_name='İsim Soyisim', blank=True)
    telefon = models.CharField(max_length=20, verbose_name="Telefon", blank=True)
    email = models.EmailField(blank=True, verbose_name="E-mail")
    subject = models.CharField(max_length=100, blank=True, verbose_name="Mesaj")

    def __str__(self):
        return self.name
    
    
    

