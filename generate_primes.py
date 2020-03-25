def check_prime(num):
    counter = 2
    if num == 1: return True
    if num == 2: return True
    for item in range(counter, num - 1):
        if num % counter == 0:
            return False
        counter += 1
    return True

def generate_prime(limit):
    items_printed = 1
    candidate_num = 1
    while True:
        if check_prime(candidate_num):
            yield items_printed, candidate_num
            items_printed = items_printed + 1
        if items_printed > limit:
            break
        candidate_num += 1
for index, prime_no in generate_prime(100):
    print("item {:03d} : {:03d}".format(index, prime_no))