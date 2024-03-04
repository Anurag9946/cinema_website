from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Movie, Category, Review
from . forms import MovieForm
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {
        'movie_list' : movies
    }
    return render(request, 'index.html', context)

def cat(request):
    cat = Category.objects.all()
    categories = {
        'cat_list' : cat
    }
    return render(request, 'index.html', categories)

def review(request):
    reviews = Review.objects.all()
    context1 = {
        'review_list' : reviews
    }
    return render(request, 'review.html', context1)




def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request, 'movie_details.html',{'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        movie_title = request.POST.get('movie_title')
        poster = request.FILES.get('poster')
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        actors = request.POST.get('actors')
        category_name = request.POST.get('category')
        trailer_link = request.POST.get('trailer')
        category, created = Category.objects.get_or_create(name=category_name)
        added_by = request.user

        movie = Movie(
            movie_title=movie_title,
            description=description,
            poster=poster,
            release_date=release_date,
            actors=actors, category=category,
            trailer_link=trailer_link,
            added_by=added_by,
        )
        movie.save()
        return redirect('/')
    return render(request, 'add.html')

def add_review(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        movie = request.POST.get('movie')
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        review = Review( user=user, movie=movie, text=text, rating=rating)
        review.save()
        return redirect('/')
    return render(request, 'add_review.html')


def update(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None,request.FILES,instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form, 'movie':movie})

def delete(request,id):
    if request.method == 'POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('filmapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('filmapp:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                return redirect('filmapp:login')
        else:
            messages.info(request, "password not macting")
            return redirect('filmapp:register')
        return redirect('/')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html', {'error': True, 'username': username})

    return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')






