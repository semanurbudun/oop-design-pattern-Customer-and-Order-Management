class Payment:
    def __init__(self, amount):
        """
        Ödeme sinifini tesmil eder.

        amount: Ödeme miktari.
        """
        self.amount = amount

    def authorized(self):
        """
        Alt siniflar tarafindan uygulanan, ödemenin yetkilendirilip yetkilendirilmediğini kontrol eden metot.
        Soyut metottur ve alt siniflarda gerçek bir içerik ile doldurulmalidir.
        """
        raise NotImplementedError("Yetkili yöntem alt siniflarda uygulanmalidir.")
    
class Cash(Payment):
    def __init__(self, amount, cashTendered):
        """
        Nakit ödeme sinifinin yapici metodu.

        amount: Ödeme miktari.
        cashTendered: Verilen nakit miktari.
        """
        super().__init__(amount)
        self.cashTendered = cashTendered

        def authorized(self):
            """
            Nakit ödemesinin yetkilendirilip yetkilendirilmediğini kontrol eden metot.

            Ödeme yetkilendirilmişse True, aksi halde False.
            """
            return True
class Check(Payment):
    def __init__(self, amount, bankID):
        """
        Çek ödeme sinifinin yapici metodu.
        amount: Ödeme miktari.
        bankID: Banka ID.
        """
        super().__init__(amount, bankID)
        self.bankID = bankID
        
    def authorized(self):
        """
        Çek ödemesinin yetkilendirilip yetkilendirilmediğini kontrol eden metot.
        Ödeme yetkilendirilmişse True, aksi halde False.
        """
        return True
    
class Credit(Payment):
    def __init__(self, amount, name, type, expDate):
        """
        Kredi karti ödeme sinifinin yapici metodu.
        amount: Ödeme miktari.
        name: Kredi karti sahibinin adi.
        type: Kredi karti türü.
        expDate: Kredi kartinin son kullanma tarihi.
        """
        super().__init__(amount)
        self.name = name
        self.type = type
        self.expDate = expDate

    def authorized(self):
        """
        Kredi karti ödemesinin yetkilendirilip yetkilendirilmediğini kontrol eden metot.
        Ödeme yetkilendirilmişse True, aksi halde False.
        """
        return True
    
# payment_factory
class PaymentFactory:
    def create_payment(self, payment_type, amount, **kwargs):
        """
        Belirtilen ödeme türüne göre bir ödeme nesnesi oluşturur.

        payment_type: Ödeme türü ("Cash", "Check" veya "Credit").
        amount: Ödeme miktari.
        kwargs: Ekstra argümanlar, ödeme türüne göre değişebilir.
        return: Oluşturulan ödeme nesnesi.
        raises ValueError: Geçersiz ödeme türü durumunda hata döndürülür.
        """
        if payment_type == "Cash":
            return Cash(amount, **kwargs)
        elif payment_type == "Check":
            return Check(amount, **kwargs)
        elif payment_type == "Credit":
            return Credit(amount, **kwargs)
        else:
            raise ValueError("Geçersiz Ödeme Türü")

def process_payment(payment_type, amount, **kwargs):
    """
    Belirtilen ödeme türüne göre bir ödeme işlemi yapar.

    payment_type: Ödeme türü ("Cash", "Check" veya "Credit").
    amount: Ödeme miktari.
    kwargs: Ekstra argümanlar, ödeme türüne göre değişebilir.
    """
    payment_factory = PaymentFactory()
    payment = payment_factory.create_payment(payment_type, amount, **kwargs)
    if payment.authorized():
        print("Ödeme Başarili")
        print("Kullanilan Ödeme Türü:", payment_type)
    else:
        print("Ödeme Başarisiz")

        