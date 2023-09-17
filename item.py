class Item:
    """
    Bir ürünü temsil eden sinif.

    """

    def __init__(self, description, price, tax_status, in_stock, shipping_weight):
        """
        Yeni bir ürün örneği oluşturur.

        Args:
            description (str): Ürünün açiklamasi.
            price (float): Ürünün fiyati.
            tax_status (str): Ürünün vergi durumu.
            in_stock (bool): Ürünün stok durumu.
            shipping_weight (float): Ürünün gönderim ağirliği.
        """
        self.description = description
        self.price = price
        self.tax_status = tax_status
        self.in_stock = in_stock
        self.shipping_weight = shipping_weight

