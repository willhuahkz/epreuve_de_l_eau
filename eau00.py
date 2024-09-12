"""
Module to print sequences of numbers
"""
def sequences_contains_same_numbers(sequence_src, sequence):
    """
    Verify if two sequences contains the same number
    """
    same_number = 0
    for number in sequence:
        for number_src in sequence_src:
            if number == number_src:
                same_number += 1
    return same_number == 3

def is_new_sequence(sequence, list_sequences):
    """
    Verify if it is a new sequence 
    """
    # do compare if there the same number in the sequence
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if i != j and sequence[i] == sequence[j]:
                return False
            j += 1
        i += 1

    for old_sequence in list_sequences:
        if sequences_contains_same_numbers(sequence, old_sequence):
            return False
    return True

def incremente_sequence(sequence):
    """
    Incremente the good 
    """
    sequence[2] += 1
    if sequence[2] == 10:
        sequence[2] = 0
        sequence[1] += 1
        if sequence[1] == 10:
            sequence[1] = 0
            sequence[0] += 1

def get_list_sequences():
    """
    Get list_sequences of numbers
    """
    sequence = [0, 1, 2]
    list_sequences = [sequence.copy()]

    while list_sequences[-1] != [7, 8, 9]:
        if is_new_sequence(sequence, list_sequences):
            list_sequences.append(sequence.copy())
        else:
            incremente_sequence(sequence)
    return list_sequences

def print_result(list_sequences):
    """
    Print list of sequences
    """
    res = ''
    for sequence in list_sequences:
        for number in sequence:
            res += str(number)
        res += ' '
    print(res)

def eau00():
    """
    Do exercise for eau00
    """
    list_sequences = get_list_sequences()

    print_result(list_sequences)

eau00()
