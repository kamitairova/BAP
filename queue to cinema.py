# count_people = 4
# bills = [25, 25, 50, 50]
# wallet = 0


nums = [5, 64, 32, 97, 2, 12345]


def find_factors(n):
    # Пробуем найти три различных множителя a, b, c
    for a in range(2, int(n ** (1/3)) + 1):
        if n % a == 0:
            n1 = n // a
            for b in range(a + 1, int(n1 ** (1/2)) + 1):
                if n1 % b == 0:
                    c = n1 // b
                    if c > b:
                        return a, b, c
    return None

def solve():
    t = int(input())  # Число наборов входных данных
    for _ in range(t):
        n = int(input())  # Значение n для текущего набора
        result = find_factors(n)
        if result:
            print("YES")
            print(*result)
        else:
            print("NO")

# Запуск функции решения
solve()

# def d_func(num, index=None, ):
#     div_i = 2
#     if index is None:
#         index = 2
#
#     if index == 2:
#         while div_i <=100:
#             if num % index == 0 and num // index >= 2:
#                 return index, num//index
#             elif num % index != 0:
#                 index += 1
#
#             else:
#                 return False, False
#     else:
#         while div_i <=100:
#             if num % index == 0 and num // index >= 2:
#                 return num//index








    # while index <= 100:
    #     if num % index == 0 and num//index >= 2:
    #         return index, num//index
    #     elif num % index != 0:
    #         index += 1
    #
    #     else:
    #         return False, False



# for i in range(len(nums)):
#     a, b = d_func(nums[i])
#     print(a,b)