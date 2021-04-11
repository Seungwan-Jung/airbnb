from django.db import models
from django.contrib.auth.models import AbstractUser

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
    avatar = models.ImageField()
    gender = models.CharField(
        choices=GENDER_CHOICE,
        max_length=10,
    )
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=2,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        max_length=4,
    )
    superhost = models.BooleanField(default=False)
