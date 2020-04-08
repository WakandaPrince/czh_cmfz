import random
def random_code():
    code = random.randrange(1000,9999)
    return code
if __name__ == '__main__':
    print(random_code())