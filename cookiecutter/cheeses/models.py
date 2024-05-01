from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField
from django.urls import reverse
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cheese(TimeStampedModel):
    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address",
        unique=True, always_update=False, populate_from="name")

    description = models.TextField("Description", blank=True)
    class Firmness(models.TextChoices):
          UNSPECIFIED = "unspecified", "Unspecified"
          SOFT = "soft", "Soft"
          SEMI_SOFT = "semi-soft", "Semi-Soft"
          SEMI_HARD = "semi-hard", "Semi-Hard"
          HARD = "hard", "Hard"
          # Other Fields Here...
    firmness = models.CharField("Firmness", max_length=20,
          choices=Firmness.choices, default=Firmness.UNSPECIFIED)

    country_of_origin = CountryField(
        "Country of Origin", blank=True
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute URL to the Cheese Detail page."""
        return reverse(
            'cheeses:detail', kwargs={"slug": self.slug}
        )

    def get_delete_url(self):
        """Return absolute URL to the Cheese Delete page."""
        return reverse(
            'cheeses:delete', kwargs={"slug": self.slug}
        )

    @property
    def average_rating(self):
        total_rating = sum(rating.rating for rating in self.rating_set.all())
        num_ratings = self.rating_set.count()
        return total_rating / num_ratings if num_ratings > 0 else 0


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)

    class Meta:
        unique_together = ('user', 'cheese')


