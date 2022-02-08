p = 1
n = 5
for i in range(1, n+1):
    print("Значение произведения на предыдущем шаге:", p)
    print("Текущее число:", i)
    p = p * i
    print("Значение произведения после умножения:", p)
    print("...")
    print("Конец цикла")
    print()
    print("Ответ: произведение равно =", p)

n = 4
for i in range (1, n+1):
    print("*" * i)

n = 1
while True:
    if n**2 >= 1000:
        print("Искомое число", n - 1)
        break
    n += 1


def check_h(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3 + 1) // 2
        if n == 1:
            return True
    return False
print(check_h(n))

def get_wind_class(speed):
    if 1 <= speed <= 4:
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return"strong [3]"
    elif speed >= 19:
        return "hurricane [4]"

print(get_wind_class(3))

def check_user(username, password):
    if username in user_database:
        if password == user_database[username]:
            return True
        else:
            return False
        else:
            return False







