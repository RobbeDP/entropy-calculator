#!/usr/bin/env python3

import sys
from entropy import Entropy


if len(sys.argv) != 3:
    print("Correct usage: python3 run.py </path/to/file> <N>")
else:
    file_path = sys.argv[1]
    n = int(sys.argv[2])

    elements = []
    with open(file_path, 'r') as file:
        for line in file:
            elements.extend(list(line))

    entropy = Entropy(elements)
    # If memory equals N, we need to consider N + 1 elements at a time.
    print(f"Entropy with N = {n}: {entropy.entropy(n + 1)}")
