import random
from datetime import date, timedelta

from django.contrib.auth.models import User
from program.models import *

def create_clients():
    clients_data = [
        {'name': 'Иванов Петр', 'phone': '+79161234567', 'address': 'ул. Ленина, 15'},
        {'name': 'Сидорова Анна', 'phone': '+79035432109', 'address': 'пр. Мира, 28к2'},
        {'name': 'Кузнецов Иван', 'phone': '+79219876543', 'address': 'ул. Садовая, 7'},
        {'name': 'Петрова Ольга', 'phone': '+79503334455', 'address': 'ш. Энтузиастов, 120'},
        {'name': 'Смирнов Дмитрий', 'phone': '+79998887766', 'address': 'ул. Пушкина, 34'},
        {'name': 'Васильева Екатерина', 'phone': '+79169998877', 'address': 'пр. Космонавтов, 11'},
        {'name': 'Николаев Артем', 'phone': '+79031112233', 'address': 'ул. Гагарина, 5'},
        {'name': 'Алексеева Мария', 'phone': '+79257778899', 'address': 'пер. Цветочный, 3'},
        {'name': 'Федоров Сергей', 'phone': '+79654443322', 'address': 'ул. Лесная, 18'},
        {'name': 'Дмитриева Алина', 'phone': '+79876543210', 'address': 'пр. Победы, 22'},
    ]
    for data in clients_data:
        Client.objects.create(**data)
    print("Создано 10 клиентов")

def create_ingredients():
    ingredients = [
        {'name': 'Картофель', 'price': 45, 'unit': 'кг'},
        {'name': 'Морковь', 'price': 55, 'unit': 'кг'},
        {'name': 'Лук', 'price': 30, 'unit': 'кг'},
        {'name': 'Говядина', 'price': 450, 'unit': 'кг'},
        {'name': 'Сметана', 'price': 80, 'unit': 'л'},
        {'name': 'Рис', 'price': 90, 'unit': 'кг'},
        {'name': 'Курица', 'price': 300, 'unit': 'кг'},
        {'name': 'Помидоры', 'price': 150, 'unit': 'кг'},
        {'name': 'Огурцы', 'price': 120, 'unit': 'кг'},
        {'name': 'Соль', 'price': 25, 'unit': 'кг'},
    ]
    for ing in ingredients:
        Ingredient.objects.create(**ing)
    print("Создано 10 ингредиентов")

def create_dishes():
    dishes_data = [
        {'name': 'Борщ', 'description': 'Традиционный украинский суп', 'price': 250},
        {'name': 'Плов', 'description': 'Узбекский рисовый плов с говядиной', 'price': 300},
        {'name': 'Салат Оливье', 'description': 'Классический новогодний салат', 'price': 180},
        {'name': 'Курица гриль', 'description': 'Запеченная курица с пряностями', 'price': 350},
        {'name': 'Щи', 'description': 'Русские щи из свежей капусты', 'price': 220},
        {'name': 'Гречка с овощами', 'description': 'Гречневая каша с тушеными овощами', 'price': 200},
        {'name': 'Котлета по-киевски', 'description': 'Куриная котлета с маслом', 'price': 280},
        {'name': 'Винегрет', 'description': 'Овощной салат с свеклой', 'price': 150},
        {'name': 'Гуляш', 'description': 'Говяжий гуляш с подливкой', 'price': 320},
        {'name': 'Суп-лапша', 'description': 'Куриный суп с домашней лапшой', 'price': 230},
    ]

    ingredients = Ingredient.objects.all()

    for data in dishes_data:
        dish = Dish.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )

        # Добавляем случайные ингредиенты (3-5 на блюдо)
        for ing in random.sample(list(ingredients), k=random.randint(3,5)):
            DishIngredient.objects.create(
                dish=dish,
                ingredient=ing,
                quantity=random.randint(100, 500)
            )
    print("Создано 10 блюд с ингредиентами")

def create_menus():
    for i in range(10):
        menu_date = date.today() + timedelta(days=i)
        menu = Menu.objects.create(date=menu_date)
        dishes = Dish.objects.order_by('?')[:5]  # 5 случайных блюд
        menu.dishes.add(*dishes)
    print("Создано 10 меню")

def create_orders():
    clients = Client.objects.all()
    statuses = ['new', 'preparing', 'delivered']

    for i in range(10):
        client = random.choice(clients)
        order = Order.objects.create(
            client=client,
            status=random.choice(statuses),
            notes=f"Примечание к заказу {i+1}",
            total=0
        )

        # Добавляем 2-5 случайных блюд
        dishes = Dish.objects.order_by('?')[:random.randint(2,5)]
        for dish in dishes:
            OrderDish.objects.create(
                order=order,
                dish=dish,
                quantity=random.randint(1,3)
            )

        order.save()  # Пересчет total
    print("Создано 10 заказов")


def create_users_and_roles():
    roles = ['manager', 'dispatcher', 'calculator']
    for i in range(3):
        user = User.objects.create_user(
            username=f'{roles[i][:3]}',
            password='123'
        )
        UserRole.objects.create(
            user=user,
            role=roles[i]
        )
    print("Создано 3 пользователя с ролями")


def main():
    create_clients()
    create_ingredients()
    create_dishes()
    create_menus()
    create_orders()
    create_users_and_roles()
    print("Все данные успешно созданы!")


if __name__ == '__main__':
    main()
