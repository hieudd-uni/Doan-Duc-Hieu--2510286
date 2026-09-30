import math

#1
radius = float(input("Enter circle radius? "))
area = math.pi * radius ** 2
print(f"Circle area = {area:.1f}")

#2
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = celsius * 1.8 + 32
print(f"{int(celsius)} (C) = {fahrenheit:.1f} (F)")

#3
import math

num = int(input("Enter a number? "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is a NOT prime number")

#4
num = int(input("Enter a number? "))
divisor_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisor_sum += i
if divisor_sum == num and num > 0:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is NOT a perfect number")

#5
colors = ["Blue", "Yellow", "Pink", "Red", "White"]
fav_color = input("What is your favorite color? ")
if fav_color in colors:
    index = colors.index(fav_color)
    print(f"Your colod is at index {index} in my list")
else:
    print("Sorry, I could not find your color")

#6
range_1 = list(range(0, 7))
print("range 1:", range_1)
range_2 = list(range(1, 11, 3))
print("range 2:", range_2)
range_3 = list(range(5, 0, -1))
print("range 3:", range_3)
range_4 = list(range(6, -3, -2))
print("range 4:", range_4)

#7
def remove_dollar_sign(s):
    return s.replace("$", "")

#8
def extract_even(l):
    return [num for num in l if num % 2 == 0]

#9
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Number must be a non-negative integer.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#10
def get_divisors(n):
    if n <= 0:
        return []
    return [i for i in range(1, n + 1) if n % i == 0]

#11
import math

def compute_distance(p1, p2):
    # p1 and p2 are tuples or lists representing (x, y) coordinates
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

#12
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " * n)
        else:
            print("* ")