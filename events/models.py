from django.db import models
from authentication.models import CustomUser

# Create your models here.



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    cover_image=models.ImageField(upload_to='event_images/', null=True, blank=True)
    location = models.CharField(max_length=255)
    participants = models.ManyToManyField(CustomUser, related_name="participating_events", through="Participant")
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    max_participants = models.IntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_available_slots(self):
        return self.max_participants - self.participants.count()
    
class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="participant_in_event")
    registered_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user    
    

    class Meta:
        unique_together = ('event', 'user')
    
    

 
