### Latihan 2
print("===== Latihan 2 =====")
import random
n = input("Masukan jumlah n - ")
for i in range(5):
    while 1:
        n = random.random()
        if n < 0.5:
            break
    print(n)