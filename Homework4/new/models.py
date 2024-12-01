from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100,verbose_name='Muallifning ismi')
    last_name = models.CharField(max_length=100, verbose_name='Muallifning familiyasi')
    date_of_birth = models.DateField(verbose_name='Tug‘ilgan sana',null=True,blank=True)
    date_of_death = models.DateField(verbose_name='Vafot etgan sana',null=True,blank=True)
    biography =models.TextField(verbose_name="Muallif haqida qisqa ma'lumot",null=True,blank=True)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kitobning nomi")
    publication_date = models.DateField(auto_now_add=True,verbose_name="Nashr sanasi")
    isbn = models.CharField(max_length=13,unique=True,verbose_name="Kitobning ISBN raqami")
    genre = models.CharField(max_length=100,verbose_name="Kitob janri")
    summary = models.TextField(null=True,blank=True,verbose_name="Kitob haqida qisqacha ma'lumot")
    photo = models.ImageField(null = True,blank=True,upload_to='photos/',verbose_name="kitob rasmini kiriting")
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100,verbose_name="yozgan foydalanuvchi ismi")
    rating = models.PositiveSmallIntegerField(10,"Kitob bahosi")
    comment = models.TextField(null= True,blank=True,verbose_name="Sharh matni")
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book,related_name='reviews',on_delete=models.CASCADE)

    def __str__(self):
        return self.reviewer_name
