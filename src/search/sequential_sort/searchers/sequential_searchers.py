def threshold_search(sequence, target):
    comparisons = 1
    if sequence[-1] == target:
        return comparisons
    
    sequence.append(target)

    while sequence[comparisons] != target:
        comparisons += 1
    
    sequence = sequence.pop()

    return comparisons

def permutation_search(sequence, target):
    comparisons = 0
    for i in range(len(sequence)):
        comparisons += 1
        if sequence[i] == target:
            if i > 0:
                sequence[0], sequence[i] = sequence[i], sequence[0]
            return comparisons
    return comparisons

def exchange_search(sequence, target):
    comparisons = 0
    for i in range(len(sequence)):
        comparisons += 1
        if sequence[i] == target:
            if i > 0:
                sequence[i], sequence[i - 1] = sequence[i - 1], sequence[i]
            return comparisons
    return comparisons