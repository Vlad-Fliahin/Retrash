from django.db import models


# Create your models here.
class Prize(models.Model):
    prize_id = models.IntegerField()
    image_url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    partner_name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return f"Prize_id:{self.prize_id}\tType:{self.type}\t" \
               f"Name:{self.name}\tPartner_name:{self.partner_name}\tType:{self.type}"


class TrashCan(models.Model):
    can_id = models.IntegerField()
    geopoint = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return f"Can_id:{self.can_id}\tGeopoint:{self.geopoint}\tStatus:{self.status}"


class User(models.Model):
    surname = models.CharField(max_length=200)
    photo_url = models.CharField(null=True, blank=True, max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    favorite_bin = models.ForeignKey(TrashCan, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200)
    points = models.IntegerField()

    def __str__(self):
        return f"Name:{self.name}\tSurname:{self.surname}\tEmail:{self.email}"


class TrashCount(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    aluminium = models.IntegerField()
    glass = models.IntegerField()
    paper = models.IntegerField()
    plastic = models.IntegerField()

    def __str__(self):
        return f"User_id:{self.user_id}\tAluminium:{self.aluminium}\tGlass:{self.glass}\t" \
               f"Paper:{self.paper}\tPlastic:{self.plastic}"

