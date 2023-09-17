class Customer:
    """
    Bir müşteriyi ad ve adres bilgisiyle temsil eder.

    """
    def __init__(self, name, address):
        
        """
        Yeni bir Müşteri örneği oluşturur.

        Args:
            name (str): Müşterinin adi.
            address (str): Müşterinin adresi.
        """
        self.name = name
        self.address = address
    
