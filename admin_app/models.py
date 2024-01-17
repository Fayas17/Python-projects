from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default='no value')
    language = models.CharField(max_length=25)
    poster = models.ImageField(upload_to ='posters', null=True, blank= True)
    trailer_video = models.FileField(upload_to='add_trailer', null=True, blank= True)
    movie_video = models.FileField(upload_to = 'add_movies', null= True, blank=True)

    def __str__(self):
        return f'{self.name} {self.year}'
    

class Genres(models.Model):
    name = models.CharField(max_length=50)
    movie_name = models.ForeignKey(Movies, on_delete = models.CASCADE, null = True, blank = True )

class Cast(models.Model):
    movie_id = models.ForeignKey(Movies, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'cast')

class Songs(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    language = models.CharField(max_length=50)
    # singer = models.CharField(max_length=100)
    song = models.FileField(upload_to='songs')


class Subscription(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField(null = True, blank = True)
    price = models.IntegerField()