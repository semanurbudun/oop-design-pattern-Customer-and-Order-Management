from customer import Customer
from item import Item
from order import Order, PaymentFactory, process_payment
from invoice import Invoice
from order_detail import OrderDetail
from payment import Payment, Cash, Check, Credit, PaymentFactory, process_payment

if __name__ == "__main__":
    customer = Customer("John Doe", "123 Main Street")

    # Ürün oluştur
    item1 = Item("Product 1", 50, "Taxable", True, 1.5)
    item2 = Item("Product 2", 25, "Non-Taxable", True, 0.8)

    # Sipariş detayları oluştur
    order_detail1 = OrderDetail(item1, 3)
    order_detail2 = OrderDetail(item2, 2)

    # Sipariş oluştur
    order = Order()

    order.set_date("2023-07-24")
    order.set_customer(customer)
    order.add_order_detail(order_detail1)
    order.add_order_detail(order_detail2)
    
    # Sipariş bilgilerini göster
    print("Sipariş Tarihi:", order.date)
    print("Müşteri:", order.customer.name)
    print("Adres:", order.customer.address)
    print("Sipariş Durumu:", order.status)
    print("Sipariş Detayları:")

    for order_detail in order.order_details:
        print("- Ürün:", order_detail.item.description)
        print("  Miktar:", order_detail.quantity)
        print("  Alt Toplam:", order_detail.calc_subtotal())
        
    # Toplam tutar ve ağırlığı göster
    print("Sipariş Toplami:", order.calc_total())
    print("Sipariş Ağirliği:", order.calc_total_weight())
    payment_factory = PaymentFactory()
    order.process_payment("Credit", amount=order.calc_total(), name="John Doe", type="Visa", expDate="12/25")

    invoice = order.create_invoice()
    invoice.generate_invoice()
    invoice.send_invoice()

    


   