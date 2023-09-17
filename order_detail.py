class OrderDetail:
    def __init__(self, item, quantity):
        """
        Yeni bir sipariş detayi öğesi oluşturur.

        Args:
            item (Item): Sipariş detayina ait ürün.
            quantity (int): Ürün miktari.
        """
        self.item = item
        self.quantity = quantity

    def calc_subtotal(self):
        """
        Sipariş detayinin ara toplamini hesaplar.

        Returns:
            float: Sipariş detayinin ara toplami.
        """
        return self.item.price * self.quantity

    def calc_weight(self):
        """
        Sipariş detayinin toplam ağirliğini hesaplar.

        Returns:
            float: Sipariş detayinin toplam ağirliği.
        """
        return self.item.shipping_weight * self.quantity

    def calc_tax(self):
        """
        Sipariş detayinin vergi tutarini hesaplar.

        Returns:
            float: Sipariş detayinin vergi tutari.
        """
        tax_rate = 0.08  # %8 vergi orani
        return self.calc_subtotal() * tax_rate


