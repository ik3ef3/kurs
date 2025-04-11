from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.phone})"


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    ingredients = models.ManyToManyField(Ingredient, through='DishIngredient')
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('dish', 'ingredient')


class Menu(models.Model):
    date = models.DateField(unique=True)
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return f"Меню на {self.date}"


class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('preparing', 'Готовится'),
        ('delivered', 'Доставлен'),
    )

    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    dishes = models.ManyToManyField(Dish, through='OrderDish')

    def update_total(self):
        self.total = sum(item.quantity * item.dish.price for item in self.orderdish_set.all())
        self.save()

    def get_status_color(self):
        return {
            'new': 'secondary',
            'preparing': 'warning',
            'delivered': 'success'
        }.get(self.status, 'light')

    def __str__(self):
        return f"Заказ #{self.id} - {self.client.name}"


class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('order', 'dish')


class UserRole(models.Model):
    ROLES = (
        ('manager', 'Менеджер'),
        ('dispatcher', 'Диспетчер'),
        ('calculator', 'Калькулятор'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
