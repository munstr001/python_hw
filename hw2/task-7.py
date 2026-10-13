class Product:
    def __init__(self, name, price, stock, category):
        if price < 0 or not isinstance(stock, int) or stock < 0:
            raise ValueError('Неверная цена или остаток')
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, product, quantity=1):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError('Количество должно быть целым положительным числом')
        self.update(product, self.items.get(product, 0) + quantity)

    def remove(self, product):
        self.items.pop(product, None)

    def update(self, product, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Неверное количество')
        if quantity > product.stock:
            raise ValueError(f'Недостаточно товара: {product.name}')
        if quantity == 0:
            self.remove(product)
        else:
            self.items[product] = quantity

    def total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def show_history(self):
        for number, order in enumerate(self.orders, 1):
            print(f'Заказ {number}: {order.total:.2f} руб.')


class Order:
    def __init__(self, customer, cart, discount=0, tax=0):
        if not cart.items:
            raise ValueError('Корзина пустая')
        if not 0 <= discount <= 100 or not 0 <= tax <= 100:
            raise ValueError('Скидка и налог задаются в процентах от 0 до 100')
        self.customer = customer
        self.discount = discount
        self.tax = tax
        self.items = []
        for product, quantity in cart.items.items():
            if quantity > product.stock:
                raise ValueError(f'Недостаточно товара: {product.name}')
            self.items.append((product.name, product.price, quantity))

        subtotal = sum(price * quantity for name, price, quantity in self.items)
        self.total = round(subtotal * (1 - discount / 100) * (1 + tax / 100), 2)
        for product, quantity in cart.items.items():
            product.stock -= quantity
        customer.orders.append(self)
        cart.items.clear()


if __name__ == '__main__':
    mouse = Product('Мышь', 1200, 10, 'Электроника')
    keyboard = Product('Клавиатура', 3000, 5, 'Электроника')
    cable = Product('Кабель', 400, 20, 'Аксессуары')
    customer = Customer('Валерий', 'valery@example.com')
    cart = ShoppingCart()
    cart.add(mouse, 2)
    cart.add(keyboard)
    cart.add(cable)
    cart.remove(cable)
    cart.update(mouse, 1)
    print('До скидки и налога:', cart.total())
    order = Order(customer, cart, discount=10, tax=20)
    print('К оплате:', order.total)
    print('Осталось мышек:', mouse.stock)
    customer.show_history()
