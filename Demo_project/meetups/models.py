from django.db import models



    
class Participant(models.Model):
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email
    
class Meetup(models.Model):
    title=models.CharField(max_length=200)
    organizer_email=models.EmailField()
    date=models.DateField()
    description=models.TextField()
    location=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    image=models.ImageField(upload_to='images')
    participants=models.ManyToManyField(Participant,null=True,blank=True)

    def __str__(self): 
        return f"{self.title}"