# 1st step:

def calculate_first_pass():
    file = give_a_file(path)
    pass_dictionary = {}
    products_with_id = assigning_ids()
    line = file.readline()
    while line:
        product = line.split(';')[0]
        if products_with_id[product] in pass_dictionary:
            pass_dictionary[products_with_id[product]] += 1
        else:
            pass_dictionary[products_with_id[product]] = 1
        line = file.readline()
    return pass_dictionary


# 2nd step:
def prepare_baskets():
    file = give_a_file(path)
    baskets = {}
    line = file.readline()
    while line:
        product = line.split(";")[0]
        basket = line.split(";")[1].strip()
        if basket in baskets:
            array = baskets[basket]
            array.append(product)
            baskets[basket] = array
        else:
            array = []
            array.append(product)
            baskets[basket] = array
        line = file.readline()
    return baskets


# 3rd step:
def assigning_ids():
    file = give_a_file(path)
    products_with_id = {}
    id = 1
    line = file.readline()
    while line:
        product = line.split(';')[0]
        if product not in products_with_id:
            products_with_id[product] = id
            id += 1
        line = file.readline()
    return products_with_id


# 4th step:
def colleting_baskets_with_product_ids():
    baskets = prepare_baskets()
    products_with_id = assigning_ids()
    baskets_with_product_ids = {}
    for basket in baskets:
        products = []
        for product in baskets[basket]:
            products.append(products_with_id[product])
        baskets_with_product_ids[basket] = products
    return baskets_with_product_ids


# 5th step:
def colleting_baskets_with_tuples():
    baskets = colleting_baskets_with_product_ids()
    baskets_with_tuples = {}
    for basket in baskets:
        array = baskets[basket]
        tuples = []
        for i in range(0, len(array) - 1):
            for j in range(i + 1, len(array)):
                tuples.append((array[i], array[j]))
        baskets_with_tuples[basket] = tuples
    return baskets_with_tuples


# 6th step:
def calculate_second_pass():
    pass_dictionary = {}
    baskets_with_tuples = colleting_baskets_with_tuples()
    k = len(assigning_ids())
    for basket in baskets_with_tuples:
        for some_tuple in baskets_with_tuples[basket]:
            hash_value = hash_function(some_tuple, k)
            if hash_value in pass_dictionary:
                dictionary_of_tuples = pass_dictionary[hash_value]
                if some_tuple in dictionary_of_tuples:
                    dictionary_of_tuples[some_tuple] += 1
                else:
                    dictionary_of_tuples[some_tuple] = 1
                pass_dictionary[hash_value] = dictionary_of_tuples
            else:
                dictionary_of_tuples = {}
                dictionary_of_tuples[some_tuple] = 1
                pass_dictionary[hash_value] = dictionary_of_tuples
    # for value in pass_dictionary:
    #     print(value, ":", pass_dictionary[value])
    return pass_dictionary


# 7th step:
def colleting_frequent_item_sets(support_level: int):
    pass1 = calculate_first_pass()
    pass2 = calculate_second_pass()
    result = set()
    singles = 0
    pairs = 0
    for element in pass1:
        if pass1[element] >= support_level:
            result.add(element)
            singles += 1
    for element in pass2:
        dictionary_of_tuples = pass2[element]
        for some_tuple in dictionary_of_tuples:
            if dictionary_of_tuples[some_tuple] >= support_level:
                result.add(some_tuple)
                pairs += 1
    print("RESULT WITH IDS: ")
    for element in result:
        print(element)
    print()
    print("SET LENGTH:", len(result))
    print("SINGLES:", singles)
    print("PAIRS:", pairs)
    print("SUPPORT LEVEL:", support_level)
    returning_values_from_id(result)


# 8th step:
def returning_values_from_id(result_with_ids):
    products_with_id = assigning_ids()
    products_with_id = {value: key for key, value in products_with_id.items()}
    result = set()
    singles = 0
    pairs = 0
    for value in result_with_ids:
        if not isinstance(value, int):
            if (products_with_id[value[0]], products_with_id[value[1]]) not in result: pairs+= 1
            result.add((products_with_id[value[0]], products_with_id[value[1]]))
        else:
            if products_with_id[value] not in result: singles += 1
            result.add(products_with_id[value])
    print()
    print("RESULT WITH DEFAULT VALUES:")
    for element in result:
        print(element)
    print()
    print("SET LENGTH:", len(result))
    print("SINGLES:", singles)
    print("PAIRS:", pairs)


# Help functions:
def hash_function(some_tuple: tuple, k):
    return (some_tuple[0] + some_tuple[1]) % k


def give_a_file(file_path: str):
    return open(file_path)


path = 'PCY_Text.txt'
support_level = int(input("ENTER SUPPORT LEVEL: "))
colleting_frequent_item_sets(support_level)
print("SUPPORT LEVEL:", support_level)

# dicti = calculate_first_pass()
# for element in dicti:
#     if dicti[element] >= 100:
#         print(element, ':', dicti[element])
