import sys

num_steps = int(sys.argv[1])
hashes = 1
spaces = num_steps - hashes

while spaces >= 0:
    result_string = " " * spaces + "#" * hashes
    print(result_string)
    hashes += 1
    spaces -= 1
