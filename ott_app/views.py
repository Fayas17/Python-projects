from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin_app.models import *
from ott_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime


def index(request):

    details = Movies.objects.all()
    context = {
        'details' : details
    }
    return render(request,'index.html',context)

# def tv_shows(request):

#     all_genres = Genres.objects.filter().values_list('name')
    
#     unique_genres = list(set(all_genres))
#     final_list = []
#     for i in unique_genres:
#         final_list.append(i[0])
    
#     details = Movies.objects.all()
#     context = {
#         'details' : details,
#         'genres' : unique_genres,
#         'final_list':final_list,
#     }
#     return render(request,'tv_shows.html',context)

def movies(request):
    # if 'u_id' in request.session:

        all_genres = Genres.objects.filter().values_list('name')
    
        unique_genres = list(set(all_genres))
        final_list = []
        for i in unique_genres:
            final_list.append(i[0])
    
        genre = Genres.objects.filter(name = 'Drama')
        details = Movies.objects.all()
        context = {
            'details' : details,
            'genres' : unique_genres,
            'final_list':final_list,
            'genre' : genre 
         }
        
        

        return render(request,'movies.html',context)

def login(request):

    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Register.objects.filter(email=username,password=password).exists():
           data = Register.objects.filter(email=username,password=password).values('name','id','phone','email').first()
           request.session['name_u'] = data['name']
           request.session['email_u'] = data['email'] 
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['phone'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           
           user = request.session.get('u_id')
           if Subscribed.objects.filter(uid = user, status = 'active').exists():
               todays_date = datetime.datetime.now()

               expiry_date = Subscribed.objects.get(uid = user, status = 'active').expiry
               subscription_id = Subscribed.objects.get(uid = user, status = 'active').pk
               todays_date = todays_date.date()
               if todays_date>expiry_date:
                   Subscribed.objects.filter(id = subscription_id).update(status = 'inactive')
            #    print()
            #    print(expiry_date)

           else:
               return redirect(pricing)
    

           return redirect('index') 
        
        elif User.objects.filter(email=username).exists():
            data = User.objects.get(email=username)
            if data.email == username and data.check_password(password):
                return redirect('admin_index')
            else:
                return redirect('login')
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    return render(request,'login.html')

def logout(request):
    del request.session['name_u']
    del request.session['email_u']
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login')

    

def register(request):

    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['conpassword']

        Register.objects.create(
            name = name,
            email = email,
            phone = phone,
            password = password
        )

    return render(request,'register.html')


def songs(request):
    return render(request,'songs.html')


def show_details(request,id):

    user = request.session.get('u_id')
    if Subscribed.objects.filter(uid = user,status= 'active').exists():

        genre_name = request.session.get('genre_name') 
        details = Movies.objects.filter(id = id)
        genre = Genres.objects.filter(movie_name = id)
        related_movies = Genres.objects.filter(name = genre_name)
    
    
        context = {
            'details' : details,
            'genre' : genre,
            'related_movies':related_movies,
        
        }
    
        return render(request,'show_details.html',context)
    else:

        return redirect(pricing)

def filtered_movies(request,name):
    request.session['genre_name'] = name
    details = Genres.objects.filter(name = name)
    context = {
        'details' : details
    }
    return render(request,'filtered_movies.html',context)

def pricing(request):

    user = request.session.get('u_id')
    condition = None
    if Subscribed.objects.filter(uid = user,status = 'active').exists():

        condition = True

    else:
        condition = False
    details = Subscription.objects.all()
    context = {
        'details' : details,
        'condition' : condition
    }

    return render(request,'pricing.html',context)
    


def purchase_plan(request,subscription_id):

    uid = request.session.get('u_id')
    plan_id = Subscription.objects.get(id = subscription_id)

    validity = plan_id.duration

    expiry = datetime.datetime.now()+datetime.timedelta(days=validity)
    Subscribed.objects.create(
        uid = Register.objects.get(id = uid),
        plan_id  = Subscription.objects.get(id = subscription_id),
        expiry = expiry,
        status = 'active'
    )
    
    
    return redirect(pricing)

