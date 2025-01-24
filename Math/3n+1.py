# Calculates the maximum number that can last until it reaches 1
# If the number reaches 1, get a new number by adding 1

from time import sleep

actual_num = 2
range_lst = []

while actual_num > 1:
    vector_num = actual_num
    range_lst.append(vector_num)

    while True:
        if vector_num == 1:
            print("\nCurrent Number:", actual_num)
            print("Range", range_lst)
            print("No. of digits :", len(range_lst))

            vector_num = 0
            range_lst = []
            actual_num += 1
            sleep(1)
            break
        elif vector_num % 2 == 0:
            vector_num = vector_num / 2
            range_lst.append(vector_num)
        else:
            vector_num = 3 * vector_num + 1
            range_lst.append(vector_num)
