from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .models import Addrecipe
from .models import Maindishes
from .models import Category
from .forms import RecipeForm,CommentForm
from .models import Comment
from qrcode import *


# Create your views here.
def Index(request):
    return render(request, 'MainApp/Index.html')


def about(request):
    return render(request, 'MainApp/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        issue = request.POST.get('issue')
        contact = Contact(name=name, email=email, phone=phone, subject=subject, issue=issue)
        contact.save()
        return HttpResponse("thanks for contact")

    else:
        return render(request, 'MainApp/contact.html')


def chinese(requset):
    return HttpResponse("this is chinese")


def italian(requset):
    return HttpResponse("this is italian")


def indian(requset):
    return HttpResponse("this is indian")


def maindishes(request):
    maindishes = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        maindishes = Maindishes.get_all_maindishes_by_categoryid(categoryID)
    else:
        maindishes = Maindishes.get_all_maindishes()
    data = {}
    data['maindishes'] = maindishes
    data['categories'] = categories
    return render(request, 'MainApp/maindishes.html', data)


def maindish2(request, id):
    context ={}
    maindish = Maindishes.objects.filter(id=id)

    maindishes= Maindishes.objects.get(id=id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            name = request.POST.get('name')
            body = request.POST.get('body')
            email=request.POST.get('email')
            comment = Comment(maindish=maindishes,name=name,body=body,email=email)
            comment.save()
            return HttpResponse("Thanks for your comment")
    else:
        comment_form=CommentForm()

    context= {'maindish': maindish[0],
              'comment_form': comment_form,
    }
    return render(request, 'MainApp/maindish2.html', context)


def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # validation
        error_message = None

        if (not firstname):
            error_message = "First Name Required !!"
        elif len(firstname) < 4:
            error_message = "First Name must be more than 4 characters!!"
        elif (not lastname):
            error_message = "Last Name Required !!"
        elif len(lastname) < 4:
            error_message = "Last Name must be more than 4 characters!!"
        elif (not username):
            error_message = "User Name Required !!"
        elif len(username) < 5:
            error_message = "Please Enter Valid Username!!"
        elif (not password):
            error_message = "Password is Required !!"
        elif len(password) < 5:
            error_message = "Password must be more than 5 characters!!"
        elif (not email):
            error_message = "Email is Required !!"
        elif len(email) < 5:
            error_message = "Please Enter Valid Email Id!!"
        elif User.objects.filter(email=email).exists():
            error_message = "Email Address is Already Registered!!"

        # saving
        if not error_message:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                             password=password)

            user.save()
            return redirect('/')

        return render(request, 'MainApp/login.html', {'error': error_message})

    else:
        return render(request, 'MainApp/login.html')


def soup(request):
    categories= Category.objects.all()
    print(categories)
    data={}
    data['categories'] = categories

    return render(request, 'MainApp/soup.html', data)


def salads(request):


    return render(request, 'MainApp/salads.html')


def appetizers(request):
    return render(request, 'MainApp/appetizers.html')


def addrecipe(request):
    context = {}

    # create object of form
    form = RecipeForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "MainApp/addrecipe.html", context)

def clientaddrecipe(request):
    context = {}

    # create object of form
    form = RecipeForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "MainApp/clientaddrecipe.html", context)
'''
    data = {}
    categories = Category.objects.all()
    data['categories'] = categories

    if request.method == "POST":
        name = request.POST.get('name')
        level = request.POST.get('level')
        img = request.FILES['img']
        category = request.POST.get('category')
        ingred = request.POST.get('ingred')
        steps = request.POST.get('steps')
        tim = request.POST.get('tim')

        maindishes = Maindishes(name=name, level=level, img=img, ingred=ingred, steps=steps, tim=tim)
        maindishes.save()
        category1=Category(id=category)
        category1.save()
        return redirect('/')

    return render(request, 'MainApp/clientaddrecipe.html',data)
'''

def signup(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # validation

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            error_message = "Invalid Username or Password!!"


    return render(request, 'MainApp/signup.html', {'error': error_message})


def comment(request, slug):
    template_name = 'MainApp/comment.html'
    maindish = get_object_or_404(Maindishes, slug=slug)
    comments = maindish.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.maindishes = maindishes
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'maindish': maindishes,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    input = None
    if request.method == 'POST':
        input = request.POST['input']
        img = make(input)
        img.save("MainApp/static/MainApp/images/test.png")

    else:
        pass
    return render(request, 'MainApp/home.html', {'input': input})

