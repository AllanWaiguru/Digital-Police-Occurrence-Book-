from django.db import models


class Suspect(models.Model):
    suspect_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    suspect_id_number = models.IntegerField()
    date_of_birth = models.DateField()
    belongings = models.TextField()
    date_booked = models.DateTimeField(auto_now_add=True)


class FingerPrint(models.Model):
    fingerprint_id = models.AutoField(primary_key=True)
    suspect_id = models.ForeignKey(Suspect, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Crime(models.Model):
    CRIME_CHOICES = (
        ("theft", "Theft"), ("accident", "Accident"), ("assault", "Assault")
    )
    crime_type = models.CharField(max_length=100, choices=CRIME_CHOICES)
    crime_id = models.AutoField(primary_key=True)
    description = models.TextField()
    penalty = models.CharField(max_length=100)
    exhibit = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Penalty(models.Model):
    penalty_id = models.AutoField(primary_key=True)
    crime_id = models.ForeignKey(Crime, on_delete=models.CASCADE, related_name="penalties")


class Bail(models.Model):
    bail_id = models.AutoField(primary_key=True)
    suspect_id = models.ForeignKey(Suspect, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class PoliceOfficer(models.Model):
    RANK_CHOICES = (
        ("inspector", "Inspector"),
        ("corporal", "Corporal"),
        ("ocs", "OCS"),
        ("ocpd", "OCPD"),
        ("base commander", "Base Commander"),
        ("constable", "Constable"),
    )
    OFFICER_GENDER_CHOICES = (
        ("female", "Female"),
        ("male", "Male")
    )
    officer_id = models.AutoField(primary_key=True)
    officer_name = models.CharField(max_length=100)
    badge_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=OFFICER_GENDER_CHOICES)
    rank = models.CharField(max_length=100, choices=RANK_CHOICES)


class Armory(models.Model):
    armor_id = models.AutoField(primary_key=True)
    armor_name = models.CharField(max_length=100)
    armor_type = models.CharField(max_length=100)
    officer_id = models.ForeignKey(PoliceOfficer, on_delete=models.CASCADE)


class Court(models.Model):
    COURT_CHOICES = (
        ("magistrates court", "Magistrates Court"),
        ("supreme court", "Supreme Court"),
        ("high court", "High Court"),
        ("court of appeal", "Court of Appeal"),
    )
    court_id = models.AutoField(primary_key=True)
    court_location = models.CharField(max_length=200)
    court_type = models.CharField(max_length=20, choices=COURT_CHOICES)


class Lawyer(models.Model):
    lawyer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    date_of_birth = models.DateField()
    court_id = models.ForeignKey(Court, on_delete=models.CASCADE)


class Judge(models.Model):
    JUDGE_LEVEL = (
        ("magistrate", "Magistrate"),
        ("judge", "Judge"),
    )
    judge_id = models.AutoField(primary_key=True)
    judge_name = models.CharField(max_length=100)
    judge_level = models.CharField(max_length=100, choices=JUDGE_LEVEL)
    court_id = models.ForeignKey(Court, on_delete=models.CASCADE)


class PoliceStation(models.Model):
    station_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    contact_info = models.TextField()
