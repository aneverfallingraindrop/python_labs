price = int(input("Цена: "))
discount = float(input("Скидка: "))
vat = float(input("VAT: "))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(
    f"База после скидки: {base:.02f} ₽ \nНДС:               {vat_amount:.02f} ₽\nИтого к оплате:    {base + vat_amount:.02f} ₽"
)
