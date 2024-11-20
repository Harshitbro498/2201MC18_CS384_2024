def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gen_rot(num):
    rotations = []
    num_str = str(num)
    length = len(num_str)
    for i in range(length):
        rotated = num_str[i:] + num_str[:i]
        rotations.append(int(rotated))
    return rotations

def is_rot_prime(num):
    if not is_prime(num):
        return False

    rotations = gen_rot(num)
    for rotation in rotations:
        if not is_prime(rotation):
            return False

    return True

number = int(input("Enter a number: "))

if is_rot_prime(number):
    print(str(number) + " is a Rotational prime.")
else:
    print(str(number) + " is not a Rotational prime.")
