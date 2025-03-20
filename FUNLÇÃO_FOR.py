# 1: Números ímpares entre 1 e 50
print("Números ímpares entre 1 e 50:")
for num in range(1, 51, 2):
    print(num)

# 2: Sequência 1, 4, 7, ..., 40
print("\nSequência de números:")
for num in range(1, 41, 3):
    print(num)

# 3: Números pares de 0 a 30, exceto 10, 20 e 30
print("\nNúmeros pares de 0 a 30 (exceto 10, 20 e 30):")
for num in range(0, 31, 2):
    if num not in [10, 20, 30]:
        print(num)
