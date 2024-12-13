from django.db import models

class User(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=250)
    roles = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Meetings(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    preset_people = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Finance(models.Model):
    details = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.price


class Inventory(models.Model):
    title = models.TextField( null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Projects(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    ownerImage = models.URLField(blank=True, null=True)
    room_image1 = models.URLField(blank=True, null=True)
    room_image2 = models.URLField(blank=True, null=True)
    room_image3 = models.URLField(blank=True, null=True)
    room_image4 = models.URLField(blank=True, null=True)
    room_image5 = models.URLField(blank=True, null=True)

    byWhomUnder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title
