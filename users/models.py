from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings
from django.core.mail import send_mail
# Create your models here.


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICE = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    LAUNGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_SPANISH = "es"

    LANGUAGE_CHOICES = (
        (LAUNGUAGE_ENGLISH, "english"),
        (LANGUAGE_KOREAN, "korean"),
        (LANGUAGE_SPANISH, "spanish"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_PESO = "peso"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
        (CURRENCY_PESO, "PESO"),
    )
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_KOREAN)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=4, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret= models.CharField(max_length=20,default="",blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail("Verify Airbnb Account", f"Verify account, this is your secert: {secret}", settings.EMAIL_FROM,[self.email],fail_silently=False,)
        return