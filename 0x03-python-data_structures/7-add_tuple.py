#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # padd tuple that ay have one digit or none
    tuple_a_padded = tuple_a + (0, 0)
    tuple_b_padded = tuple_b + (0, 0)

    sum_at_index_0 = tuple_a_padded[0] + tuple_b_padded[0]
    sum_at_index_1 = tuple_a_padded[1] + tuple_b_padded[1]

    return (sum_at_index_0, sum_at_index_1)
