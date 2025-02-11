from itertools import permutations

def generate_strings():
    chars = "catdog"

    for perm in permutations(chars):
        print("".join(perm))

# Run the function
generate_strings()