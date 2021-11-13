### pratikum 2
print("==== Tugas pratikum 2 ====")
a = int(input("Masukkan a:"))
b = int(input("Masukkan b:"))
c = int(input("Masukkan c:"))
maks = 0

print(a, b, c)
if a > b:
    maks = a
else:
    maks = b

if c > maks:
    maks = c
print("terbesar: ", maks)


data = []
maks = 0
for i in range(6):
    x = int(input("Masukkan Bilangan:"))
    data.append(x)
    maks = x
print("Bilangan terbesar: ", maks)
