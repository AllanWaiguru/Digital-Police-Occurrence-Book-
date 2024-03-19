from django.contrib import admin

from .models import (
    Suspect,
    FingerPrint,
    Crime,
    Penalty,
    Bail,
    PoliceOfficer,
    Armory,
    Court,
    Lawyer,
    Judge,
    PoliceStation,
)


@admin.register(Suspect)
class SuspectAdmin(admin.ModelAdmin):
    pass


@admin.register(FingerPrint)
class FingerPrintAdmin(admin.ModelAdmin):
    pass


@admin.register(Crime)
class CrimeAdmin(admin.ModelAdmin):
    pass


@admin.register(Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    pass


@admin.register(Bail)
class BailAdmin(admin.ModelAdmin):
    pass


@admin.register(PoliceOfficer)
class PoliceOfficerAdmin(admin.ModelAdmin):
    pass


@admin.register(Armory)
class ArmoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    pass


@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    pass


@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    pass


@admin.register(PoliceStation)
class PoliceStationAdmin(admin.ModelAdmin):
    pass
