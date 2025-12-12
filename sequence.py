print("Введите последовательность целых чисел (оканчивающуюся нулём);")

total_sum = 0
count = 0

while True:
 num = int(input("Введите число; "))
 if num == 0:
   break
 total_sum += num
 count += 1

print(f"\nСумма всех чисел; {total_sum}")
print(f"Количество чисел; {count}")
