class Invoice:
    """ 
       Siparişe dayali olarak bir fatura oluşturmayi ve göndermeyi sağlar.
    """
    def __init__(self, order):
        """
        Yeni bir Fatura örneği oluşturur.

        Args:
            order (Order): Faturanin oluşturulacaği sipariş nesnesi.
        """
        self.order = order
        
    def generate_invoice(self):

        """
        Fatura bilgilerini oluşturarak ekrana yazdirir.
        """
        print("Fatura Oluşturuldu.")
        print("Sipariş Tarihi:", self.order.date)
        print("Müşteri:", self.order.customer.name)
        print("Adres:", self.order.customer.address)
        print("Sipariş Durumu:", self.order.status)
        print("Sipariş Detaylari:")

        for order_detail in self.order.order_details:
            print("- Ürün:", order_detail.item.description)
            print("- Miktar:", order_detail.quantity)
            print("- Alt Toplam:", order_detail.calc_subtotal())
        print("Sipariş Toplami:", self.order.calc_total())
    
    def send_invoice(self):

        """
        Oluşturulan faturayi gönderdiğini simüle eder.
        """
        print("Fatura Gönderildi")