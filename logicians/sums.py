from sets import Set
from operator import add
from operator import mul

LOWER_BOUND = 1
UPPER_BOUND = 10
LAST_ROUND = 6
bounds = range(LOWER_BOUND, UPPER_BOUND)
op_strings = {
    mul: 'Pete',
    add: 'Susan',
    }


def legal_components(remaining_candidates, op):
    components = Set()
    for op_outcome in remaining_candidates:
        for i in bounds:
            for j in bounds:
                if op(i, j) == op_outcome:
                    components.add((i, j))
    return components


def one_unique_pair(x, op, possible_components):
    count = 0
    for i, j in possible_components:
        if op(i, j) == x:
            count += 1
    return count <= 2


def check_possible_answers(removed_elements, pair_op, lc):
    if len(removed_elements) == 1:
        for el in removed_elements:
            print "Possible answer for " + op_strings[pair_op] + ": " \
                + str(el)
            for pair in lc:
                if pair_op(pair[0], pair[1]) == el:
                    print "Corresponding argument pair: " +\
                        ', '.join([str(s) for s in pair])
                    break


def update_set(component_results, component_op, current_set, pair_op):
    lc = legal_components(component_results, component_op)
    set_copy = Set(current_set)
    removed_elements = Set()
    for x in current_set:
        if only_one_pair(x, pair_op, lc):
            removed_elements.add(x)
            set_copy.remove(x)

    check_possible_answers(removed_elements, pair_op, lc)
    return set_copy


def print_round(current_round):
    print "\nRound: " + str(current_round)


def print_sets(sums, products):
    print "Sums: " + ', '.join([str(s) for s in sums])
    print "Products: " + ', '.join([str(p) for p in products])


products = Set([i * j for i in bounds for j in bounds])
sums = Set([i + j for i in bounds for j in bounds])
print_sets(sums, products)
first_round = 1
print_round(first_round)
products = update_set(products, mul, products, mul)
sums = update_set(sums, add, sums, add)
sums = update_set(products, mul, sums, add)
print_sets(sums, products)

for new_round in xrange(first_round + 1, LAST_ROUND + 1):
    print_round(new_round)
    products = update_set(sums, add, products, mul)
    sums = update_set(products, mul, sums, add)

    print_sets(sums, products)
