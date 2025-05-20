n = int(input())
people = 2

for i in range(n):
    if input().lower()[-4:] == "+one":
        people += 1
    people += 1

if people == 13:
    people += 1
print(people * 100)
