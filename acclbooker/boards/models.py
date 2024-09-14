from django.db import models
from rooms.models import Room  
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    begins =  models.TimeField()
    date =  models.DateField()
    ends =  models.TimeField()
    user =  models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.ends and self.begins and self.ends < self.begins:
            raise ValidationError('The end time cannot be earlier than the start time.')
        
        # Check if the ends date is after the begins date
        if self.ends <= self.begins:
            raise ValidationError('End time must be after start time.')

        # Check for overlapping boards
        overlapping_boards = Board.objects.filter(
            begins__lt=self.ends,
            ends__gt=self.begins,
            room=self.room,
            is_completed=False,
            date=self.date
        ).exclude(id=self.id)  # Exclude the current instance if it’s being updated

        if overlapping_boards.exists():
            raise ValidationError('This board time you set is already taken.')
        
    def save(self, *args, **kwargs):
        self.clean()  # Ensure that validation is enforced before saving
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]


    def __str__(self):
        return self.title
