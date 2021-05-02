number = int(input("Bir sayı giriniz: "))  #AMICABLE NUMBERS
bölenler1 = []
bölenler2 = []

for i in range(1,number):
    if number%i == 0:
        bölenler1.append(i)

toplam_bölenler1 = sum(bölenler1)

for k in range(1,toplam_bölenler1):
  if toplam_bölenler1 % k == 0:
    bölenler2.append(k)

toplam_bölenler2 = sum(bölenler2)

if number == toplam_bölenler2:
  print("your number is amicable")
else:
  print("your number is not amicable")  