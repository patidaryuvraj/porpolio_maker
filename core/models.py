from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=50, verbose_name="Your Name ")
    age = models.IntegerField(verbose_name="Your Age ")
    dob = models.DateField(verbose_name="Date of Birth ")
    mobile = models.CharField(max_length=15, verbose_name="Your Mobile ")
    email = models.EmailField(max_length=75, verbose_name="Your Email ")
    city = models.CharField(max_length=50, verbose_name="Your City ")
    website = models.CharField(max_length=40, verbose_name="Your Website ")
    degree = models.CharField(max_length=40, verbose_name="Your Qualification ")
    profile = models.CharField(max_length=40, verbose_name="Your Profile ")
    short_desc = models.TextField(max_length=200, verbose_name="Your Short_description ")
    desc = models.TextField(max_length=600, verbose_name="Your Description ")
    pimg = models.ImageField(upload_to="about", verbose_name="Your Imagee ")


    class Meta:
        db_table = "about"

class Skill(models.Model):
    tech = models.CharField(max_length=20,verbose_name="Add your Skill ")
    rate = models.IntegerField(verbose_name="Rate your self in % ")
    desc = models.TextField(max_length=200,verbose_name="Skill description ")

    class Meta:
        db_table = "skill"


class Education(models.Model):
    degree = models.CharField(max_length=50, verbose_name="Degree ")
    year = models.CharField(max_length=20, verbose_name="Duration of Degree ")
    university = models.CharField(max_length=75, verbose_name="University Name ")
    desc = models.TextField(max_length=300,verbose_name="Education Description ")

    class Meta:
        db_table = "education"

class Experience(models.Model):
    profile = models.CharField(max_length=50, verbose_name="profile ")
    year = models.CharField(max_length=20, verbose_name="Total Experience ")
    company_name = models.CharField(max_length=75, verbose_name="Company Name ")
    desc = models.TextField(max_length=300,verbose_name="Exprience Description ")

    class Meta:
        db_table = "exprience"

class Portpolio(models.Model):
    title = models.CharField(max_length=70, verbose_name="Portpolio title ")
    desc = models.TextField(max_length=500, verbose_name="Portpolio Description ")
    image = models.ImageField(upload_to="portpolio", verbose_name="Portpolio Image ")

    class Meta:
        db_table = "portfolio"

class Service(models.Model):
    title = models.CharField(max_length=70,verbose_name="Service Name ")
    desc = models.TextField(max_length=500, verbose_name="Service Description ")

    class Meta:
        db_table = "service"

class Testimonial(models.Model):
    name = models.CharField(max_length=70,verbose_name="Name ")
    profile = models.CharField(max_length=50, verbose_name="profile ")
    desc = models.TextField(max_length=500, verbose_name="Description ")
    image = models.ImageField(upload_to="testimonial", verbose_name="Image ")

    class Meta:
        db_table = "testimonial"

class Contactus(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    subject = models.TextField(max_length=55)
    message = models.TextField(max_length=500)

    class Meta:
        db_table = "contact"


