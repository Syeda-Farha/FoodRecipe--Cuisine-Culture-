from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.forms import ModelForm


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=70)
    issue = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Addrecipe(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    file = models.ImageField(upload_to='MainApp/static/MainApp/images')


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


class Login(models.Model):
    username=models.CharField(max_length=50,default="New")
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

    @staticmethod
    def get_user_by_email(email):
        return Login.objects.get(email=email)

    def isExists(self):
        if Login.objects.filter(email=self.email):
            return True
        else:
            return False



class Maindishes(models.Model):

    name = models.CharField(max_length=60)
    img = models.ImageField(upload_to='MainApp/static/MainApp/images')
    level = models.CharField(max_length=60)
    ingred = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    steps = models.TextField(default='')
    tim = models.CharField(max_length=10)
    slug=models.SlugField(null=True)



    def __str__(self):
        return self.name


    @staticmethod
    def get_all_maindishes():
        return Maindishes.objects.all()

    @staticmethod
    def get_all_maindishes_by_categoryid(category_id):
        if category_id:
            return Maindishes.objects.filter(category=category_id)
        else:
            return Maindishes.get_all_maindishes();

    @staticmethod
    def get_maindishes_by_recipeid(id):
        if id:
            return Maindishes.objects.filter(maindishes=id)
        else:
            return Maindishes.get_all_maindishes();

class Comment(models.Model):
    maindish = models.ForeignKey(Maindishes,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)





