from django.shortcuts import render,redirect
from admin_app.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# -------------------Index page-------------------

def admin_index(request):
    return render(request,'admin_index.html')

# -------------------End of Index page-------------------


# -------------------Add Genres-------------------

def movie_genres(request):
    if request.method == "POST":
        name = request.POST['genres'].title()
        movie_name = request.POST['movie_name']

        Genres.objects.create(
            
            movie_name = Movies.objects.get(id = movie_name),
            name = name
            
        )
    
    movies = Movies.objects.all()
    context = {
        'movies' : movies
    }

    return render(request,'forms/movie_genres.html',context)

# -------------------Genre Card-------------------

def genre_card(request):    

    details = Movies.objects.all()
    context = {
        'details' : details,
    }

    return render(request,'cards/genre_card.html',context)

# -------------------View Genres-------------------

def view_genres(request,id):

    details = Genres.objects.filter(movie_name = id)
    context = {
        'details' : details
    }

    return render(request,'tables/view_genres.html',context)

# -------------------Delete Genres-------------------

def del_genres(request,id):
    Genres.objects.filter(id = id).delete()
    return redirect('genre_card')

# -------------------End Genres-------------------

# -------------------Add Movies-------------------

def add_movies(request):
    if request.method == 'POST':
        name = request.POST['moviename']
        year = request.POST['movieyear']
        language = request.POST['movielang']
        poster = request.FILES['image']
        trailer = request.FILES['trailer']
        video = request.FILES['video']

        Movies.objects.create(
            name = name,
            year = year,
            language = language,
            poster = poster,
            trailer_video = trailer,
            movie_video = video,
        )

    return render(request,'forms/add_movies.html')

# -------------------View Movies-------------------

def view_movies(request):

    details = Movies.objects.all()
    context = {
        'details' : details
    } 
    return render(request,'tables/view_movies.html',context)

# -------------------Edit Movies-------------------

def edit_movies(request,id):
    details = Movies.objects.filter(id = id)
    context = {
        'details' : details
    }
    if request.method == 'POST':
        name = request.POST['moviename']
        year = request.POST['movieyear']
        language = request.POST['movielang']

        try:
            poster = request.FILES['newImage']
            fs = FileSystemStorage()
            file = fs.save(poster.name,poster)
        except MultiValueDictKeyError:
            file = Movies.objects.get(id = id).poster
        
        try:
            trailer = request.FILES['newtrailer']
            fs1 = FileSystemStorage()
            file1 = fs1.save(trailer.name,trailer)
        except MultiValueDictKeyError:
            file1 = Movies.objects.get(id = id).trailer_video 

        try:
            video = request.FILES['newVideo']
            fs2 = FileSystemStorage()
            file2 = fs2.save(video.name,video)
        except MultiValueDictKeyError:
            file2 = Movies.objects.get(id = id).movie_video

        Movies.objects.filter(id = id).update(
            name = name,
            year = year,
            language = language,
            poster = file,
            trailer_video = file1,
            movie_video = file2,
        )
        return redirect('view_movies')
    return render(request,"forms/edit_movies.html",context)

# -------------------Delete Movies-------------------

def del_movies(request,id):
    Movies.objects.filter(id = id).delete()
    return redirect('view_movies')

# -------------------End of Movies-------------------

# -------------------Add Cast------------------

def add_cast(request):

    if request.method == 'POST':
        name = request.POST["castname"].title()
        image = request.FILES["image"]
        movie_id = request.POST['movie_id']

        Cast.objects.create(
            
            movie_id = Movies.objects.get(id = movie_id),
            name = name,
            image = image
        )
    
    movies = Movies.objects.all()
    context = {
        'movies':movies
    }


    return render(request,'forms/add_cast.html',context)

# -------------------Cast Card-------------------

def cast_card(request):

    details = Movies.objects.all()
    context = {
        'details' : details
    }

    return render(request,'cards/cast_card.html',context)

# -------------------View Cast-------------------

def view_cast(request,id):
    
    details = Cast.objects.filter(movie_id = id)
    context = {
        'details' : details
    }

    return render(request,'tables/view_cast.html',context)

# -------------------Edit Cast-------------------

def edit_cast(request,id):

    details = Cast.objects.filter(id = id)
    context = {
        'details' : details
    }
    if request.method == 'POST':
        name = request.POST['castname']
        try:
            image = request.FILES['newImage']
            fs = FileSystemStorage()
            file = fs.save(image.name,image)
        except MultiValueDictKeyError:
            file = Cast.objects.get(id = id).video

        Cast.objects.filter(id = id).update(
            name = name,
            image = file,
        )
        return redirect('view_cast')
    return render(request,"forms/edit_cast.html",context)

# -------------------Delete Cast-------------------

def del_cast(request,id):
    Cast.objects.filter(id = id).delete()
    return redirect('view_cast')

# -------------------End of Cast-------------------

# -------------------Add Songs-------------------

def add_songs(request):
    if request.method == 'POST':
        name = request.POST['songname']
        year = request.POST['songyear']
        language = request.POST['songlang']
        audio = request.FILES['audio']

        Songs.objects.create(
            name = name,
            year = year,
            language = language,
            song = audio,
        )

    return render(request,'forms/add_songs.html')

# -------------------View Songs-------------------


def view_songs(request):
    
    details = Songs.objects.all()
    context = {
        'details' : details
    }

    return render(request,'tables/view_songs.html',context)


# -------------------Edit Songs-------------------

def edit_songs(request,id):

    details = Songs.objects.filter(id = id)
    context = {
        'details' : details
    }

    if request.method == 'POST':
        name = request.POST['songname']
        year = request.POST['songyear']
        language = request.POST['songlang']
        try:
            audio = request.FILES['newAudio']
            fs = FileSystemStorage()
            file = fs.save(audio.name,audio)
        except MultiValueDictKeyError:
            file = Songs.objects.get(id = id).audio

        Songs.objects.filter(id = id).update(
            name = name,
            year = year,
            language = language,
            song = file
        )
        return redirect('view_songs')
    return render(request,"forms/edit_songs.html",context)

# -------------------Delete Songs-------------------    

def del_songs(request,id):
    Songs.objects.filter(id = id).delete()
    return redirect('view_songs')

# -------------------End of Songs-------------------


def subscription(request):
    if request.method == 'POST':
        name = request.POST['planname']
        duration = request.POST['duration']
        price = request.POST['price']

        Subscription.objects.create(
            name = name,
            duration = duration,
            price = price ,
          
        )

    return render(request,'forms/subscription.html')

def view_plans(request):
    
    details = Subscription.objects.all()
    context = {
        'details' : details
    }

    return render(request,'tables/view_plans.html',context)

def edit_plans(request,id):

    details = Subscription.objects.filter(id = id)
    context = {
        'details' : details
    }

    if request.method == 'POST':
        name = request.POST['planname']
        duration = request.POST['duration']
        price = request.POST['price']

        Subscription.objects.filter(id = id).update(
            name = name,
            duration = duration,
            price = price
        )
        return redirect('view_plans')
    return render(request,"forms/edit_plans.html",context)


def del_plans(request,id):
    Subscription.objects.filter(id = id).delete()
    return redirect('view_plans')
