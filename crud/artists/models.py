from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Music(models.Model):
    title = models.CharField(max_length=50, null=True)
    duration = models.DecimalField(decimal_places=2, max_digits= 100000)
    spotify_published = models.BooleanField(null=True)
    youtube_published = models.BooleanField(null=True)
    foreign_key = models.ForeignKey(Artist, null=True, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.title

    def getMusicsOfArtist(ArtistName):
        get_artist = Artist.objects.get(name=ArtistName)
        musics_dict = [entry for entry in (Music.objects.filter(foreign_key=get_artist).values())]
        return musics_dict