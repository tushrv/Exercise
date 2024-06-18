class EcommerceOrder:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def apply_discount(self, discount):
        for item in self.items:
            item['price'] -= item['price'] * discount / 100

    def generate_invoice(self):
        total = self.calculate_total()
        return f"Order ID: {self.order_id}\nTotal: ${total:.2f}"
        
if __name__ == '__main__':
    order = EcommerceOrder(123, [
        {'name': 'Laptop', 'price': 1200, 'quantity': 1},
        {'name': 'Mouse', 'price': 50, 'quantity': 2}
    ])
    order.apply_discount(10)
    print(order.generate_invoice())

