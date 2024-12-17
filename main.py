def sieve_of_eratosthenes(n):
    """Решето Эратосфена для нахождения всех простых чисел до n."""
    primes = [True] * (n + 1)  # Создаём список для пометки чисел
    primes[0] = primes[1] = False  # 0 и 1 не являются простыми числами
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]

def main():
    print("Решето Эратосфена для нахождения простых чисел")
    num = int(input("Введите натуральное число: "))
    primes = sieve_of_eratosthenes(num)
    print(f"Простые числа до {num}: {primes}")

if __name__ == "__main__":
    main()
