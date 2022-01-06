from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile


REM_CHOICE = (
    ("0", "Select"),
    ("Daily", "Daily"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
    ("Week before", "Week before"),
    ("Custom", "Custom"),
)


class my_task(models.Model):
    # club_name = models.CharField(max_length=20,choices=CLUB_CHOICE)
    club_name = Profile.club_name
    title = models.CharField(max_length=20)
    description = models.TextField()
    # target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    # target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()),blank=True,null=True)
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    remainder_date = models.DateField(default=timezone.localtime(timezone.now(
    )), blank=True, null=True, help_text="add date only if remainder type is custom")
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()),)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # notifications=models.CharField(max_length=500,default="")
    announcements=models.TextField(default="",null=True,blank=True,help_text="announcements should be seperated by comma, so that we can list them as points")
    resources_upload = models.FileField(upload_to='media/',blank=True,null=True)

    rsvp_users = models.ManyToManyField(Profile,related_name="rsvp_tasks")

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})

    def get_all_rsvp_users(self):
        return self.rsvp_users.all()


# rename to old_models.py
# make a new models.py
# expain why to do this
# do this for all files
