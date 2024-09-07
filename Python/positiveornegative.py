value = int(input("Bir Sayı giriniz: "))

if value > 0:
    print(f"Girdiğiniz sayı {value}, 0'dan büyüktür.")
elif value < 0:
    print(f"Girdiğiniz sayı {value}, 0'dan küçüktür.")
else:
    print(f"Girdiğiniz sayı {value}, 0'dır.")
    