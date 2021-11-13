### tugas pratikum 1
print("===== Tugas =====")
a = int(input("Masukan a:"))
b = int(input("Masukan b:"))
c = int(input("Masukan c:"))
maks = 0

print(a, b, c)
if a > b:
    maks = a
else:
    maks = b
if c > maks:
    maks = c
print("terbesar: ", maks)