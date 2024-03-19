from django.db import models



class PoliceOfficer(models.Model):
    officer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    rank = models.CharField(max_length=100)
    badge_number = models.CharField(max_length=50)

class Suspect(models.Model):
    suspect_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    date_of_birth = models.DateField()

class FingerPrint(models.Model):
    fingerprint_id = models.AutoField(primary_key=True)
    suspect_id =  models.ForeignKey(Suspect, on_delete=models.CASCADE)
    # Other fields of RelatedModel



class Crime(models.Model):
    CRIME_CHOICES = (
        ("theft","Theft"),("accident","Accident"),("assault","Assault")
    )
    CRIMES = models.CharField(max_length=50)
    crime_id = models.AutoField(primary_key=True)
    description = models.TextField()
    penalty = models.CharField(max_length=100)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    notes = models.TextField()
    police_officer = models.ForeignKey(PoliceOfficer, on_delete=models.CASCADE)
    offender = models.ForeignKey(Offender, on_delete=models.CASCADE)
    offence = models.ForeignKey(Offence, on_delete=models.CASCADE)

class PoliceStation(models.Model):
    station_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    contact_info = models.TextField()

class Court(models.Model):
    court_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    judge_info = models.TextField()

    class Meta:
        verbose_name_plural = "Courts"

