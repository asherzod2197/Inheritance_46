# 46. Mobil ilova obunalari

class Subscription:
    def __init__(self, sub_type, price):
        self.sub_type = sub_type      # "Oylik", "Yillik", "3 oylik" va h.k.
        self.price = price            # narx ($)

    def get_price(self):
        """Obuna narxi"""
        return self.price

    def __str__(self):
        period = " / oy" if "Oylik" in self.sub_type else " / yil" if "Yillik" in self.sub_type else ""
        return f"{self.sub_type:14} | {self.price:7.2f}${period}"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class MonthlySubscription(Subscription):
    def __str__(self):
        return f"📅 {self.sub_type:12} → {self.price:7.2f}$ / oy"


class YearlySubscription(Subscription):
    def __str__(self):
        return f"📆 {self.sub_type:12} → {self.price:7.2f}$ / yil"


# Qo‘shimcha misollar uchun (foydali bo‘lishi mumkin)
class QuarterlySubscription(Subscription):
    def __str__(self):
        return f"🗓️ {self.sub_type:12} → {self.price:7.2f}$ / 3 oy"


# --------------------------------------------------
# Obuna narxlarini chiqarish
# --------------------------------------------------

def show_subscription_prices(subscriptions):
    print("\n" + "═" * 60)
    print("     MOBIL ILOVA OBUNALARI — NARX RO‘YXATI     ".center(60))
    print("═" * 60)
    print("Obuna turi                  Narxi")
    print("─" * 60)

    total_monthly_equiv = 0
    yearly_count = 0

    for sub in subscriptions:
        print(sub)
        
        price = sub.get_price()
        if "Yillik" in sub.sub_type:
            monthly_equiv = price / 12
            total_monthly_equiv += monthly_equiv
            yearly_count += 1
        elif "Oylik" in sub.sub_type:
            total_monthly_equiv += price

    print("─" * 60)
    print(f"Jami obunalar narxi (ko‘rsatilgan muddatlarda): {sum(s.get_price() for s in subscriptions):8.2f}$")

    if yearly_count > 0:
        print(f"O‘rtacha oylik ekvivalent (yillik obunalar hisobida): {total_monthly_equiv / (len(subscriptions) - yearly_count + yearly_count * 12):6.2f}$ / oy")

    print("═" * 60 + "\n")


# Test ma'lumotlari
obunalar = [
    MonthlySubscription("Oylik (Premium)", 9.99),
    YearlySubscription("Yillik (Premium)", 79.99),     # ~6.67$/oy
    MonthlySubscription("Oylik (Pro)", 14.99),
    YearlySubscription("Yillik (Family)", 119.99),     # oilaviy paket
]

show_subscription_prices(obunalar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol obunalaringiz:\n")
misol_obunalar = [
    MonthlySubscription("Oylik", 10),
    YearlySubscription("Yillik", 100),
]

show_subscription_prices(misol_obunalar)
