import random

def generate_random_sequence(length):
    sequence = [i for i in range(length)]
    random.shuffle(sequence) 
    return sequence

def generate_duplicate_sequence(length, duplicate=100):
    sequence = [duplicate for _ in range(length)]
    return sequence

def generate_distribution_sequence(length, interval=100):
    sequence = []

    duplicates = generate_duplicate_sequence(interval)

    while len(sequence) < length:
        randoms = generate_random_sequence(interval)
        sequence += randoms + duplicates

    return sequence[:length]