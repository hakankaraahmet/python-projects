birler_basamağı = ["bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar_basamağı = ["on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
yüzler_basamağı = ["yüz","ikiyüz","üçyüz","dörtyüz","beşyüz","altıyüz","yediyüz","sekizyüz","dokuzyüz"]
def okunuş(number):
    yüzler = number // 100
    son_iki_basamak = number % 100
    onlar = son_iki_basamak // 10
    birler = son_iki_basamak % 10
    print(yüzler_basamağı[yüzler-1]+onlar_basamağı[onlar-1]+birler_basamağı[birler-1])