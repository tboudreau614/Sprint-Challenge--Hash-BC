#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        weight = weights[i]
        hash_table_insert(ht, weight, i)

    for i in range(length):
        weight = weights[i]
        other_weight = limit - weight
        print(f'Weight {weight}')
        print(f'Remaining {other_weight}')
        print(f'Found {hash_table_retrieve(ht, other_weight)}')
        if hash_table_retrieve(ht, other_weight):
            return [hash_table_retrieve(ht, other_weight), i]
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
