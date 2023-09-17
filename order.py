from customer import Customer
from item import Item
from invoice import Invoice
from order_detail import OrderDetail
from payment import Payment, Cash, Check, Credit, PaymentFactory, process_payment

class Order:
    """
    Bu sinif bir siparisi temsil eder. Siparis tarihi, müsteri bilgileri,
    siparis detaylari gibi özelliklere sahiptir ve ödeme islemleri yapabilir.
    """
    def __init__(self):
        """
        Yeni bir siparis örneği olusturur.
        """
        self.date = None
        self.status = "Alinan Siparis"
        self.customer = None
        self.order_details = []

    def set_date(self, date):
        """
        Siparisin tarihini ayarlar.

        Args:
            date (str): Siparis tarihi.
        """
        self.date = date

    def set_customer(self, customer):
        """
        Siparisin müsterisini ayarlar.

        Args:
            customer (Customer): Siparisin müsterisi.
        """
        self.customer = customer
    
    def add_order_detail(self, order_detail):
        """
        Siparis detayini ekler.

        Args:
            order_detail (OrderDetail): Siparis detayi öğesi.
        """
        self.order_details.append(order_detail)

    def calc_subtotal(self):
        """
        Siparisin ara toplamini hesaplar.

        Returns:
            float: Siparisin ara toplami.
        """
        subtotal = 0
        for order_detail in self.order_details:
            subtotal += order_detail.calc_subtotal()
        return subtotal

    def calc_tax(self):
        """
        Siparisin vergi tutarini hesaplar.

        Returns:
            float: Siparisin vergi tutari.
        """
        tax = 0
        for order_detail in self.order_details:
            tax += order_detail.calc_tax()
        return tax

    def calc_total(self):
        """
        Siparisin toplam tutarini hesaplar.

        Returns:
            float: Siparisin toplam tutari.
        """
        total = self.calc_subtotal() + self.calc_tax()
        return total

    def calc_total_weight(self):
        """
        Siparisin toplam ağirliğini hesaplar.

        Returns:
            float: Siparisin toplam ağirliği.
        """
        total_weight = 0
        for order_detail in self.order_details:
            total_weight += order_detail.calc_weight()
        return total_weight

    def create_invoice(self):
        """
        Siparise ait bir fatura olusturur.

        Returns:
            Invoice: Olusturulan fatura nesnesi.
        """
        invoice = Invoice(self)
        return invoice
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    def process_payment(self, payment_type, amount, **kwargs):
        """
        Belirtilen ödeme türüne göre bir ödeme islemi yapar.

        payment_type: Ödeme türü ("Cash", "Check" veya "Credit").
        amount: Ödeme miktari.
        kwargs: Ekstra argümanlar, ödeme türüne göre değisebilir.
        """
        payment_factory = PaymentFactory()
        payment = payment_factory.create_payment(payment_type, amount, **kwargs)
        if payment.authorized():
            print("*****Ödeme Basarili*****")
            print("Kullanilan Ödeme Türü:", payment_type)
        else:
            print("Ödeme Basarisiz")
    

    

