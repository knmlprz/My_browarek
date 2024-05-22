from django.db import models

CRAFT = "CR"
NORMAL = "RE"

CRAFT_REGULAR_CHOICES = [
    (CRAFT, "Craft"),
    (NORMAL, "Normal"),
]


class BeerModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    alcohol = models.FloatField()
    price = models.FloatField()
    color_type = models.CharField(max_length=20)
    image = models.ImageField(upload_to="beers")
    extract_content = models.FloatField()
    ibu = models.FloatField()
    style = models.CharField(max_length=100)
    pasteurized = models.BooleanField()
    craft_regular = models.CharField(
        max_length=2,
        choices=CRAFT_REGULAR_CHOICES,
        default=NORMAL,
    )

    def __str__(self):
        return self.name
