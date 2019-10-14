#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i, item in enumerate(weights):
        result = hash_table_retrieve(ht, limit - item)

        if result is not None:
            if i > result:
                set_result = (i, result)
            else:
                set_result = (result, i)
            return set_result
        else:
            hash_table_insert(ht, item, i)

    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
