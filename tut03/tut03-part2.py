def permutations(string):
    n = len(string)
    result = []
    indices = list(range(n))

    while True:
        result.append(''.join(string[i] for i in indices))

        i = n - 2
        while i >= 0 and indices[i] >= indices[i + 1]:
            i -= 1

        if i < 0:
            break

        j = n - 1
        while indices[j] <= indices[i]:
            j -= 1

        indices[i], indices[j] = indices[j], indices[i]
        indices = indices[:i + 1] + indices[i + 1:][::-1]

    return result

def main():
    input_string = input("Enter a string: ")
    perms = permutations(input_string)

    print("Permutations of '" + input_string + "':")
    for perm in perms:
        print(perm)

if __name__ == "__main__":
    main()

