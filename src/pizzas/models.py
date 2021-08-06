from django.db import models

TYPE_CHOICES = (("1", "Round"), ("2", "Square"))


class Topping(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)
        verbose_name = "size"
        verbose_name_plural = "sizes"

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES,
        default="round",
    )
    size = models.ManyToManyField(Size, related_name="pizzas")
    topping = models.ManyToManyField(Topping, related_name="pizzas")

    REQUIRED_FIELDS = ["type", "size", "topping"]

    def __str__(self):
        return str.name
