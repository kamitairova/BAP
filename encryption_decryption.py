def convert_base(number, from_base, to_base):
    value = int(number, from_base)

    if to_base == 10:
        return str(value)

    result = ''
    while value > 0:
        result = str(value % to_base) + result
        value //= to_base

    return result if result != '' else '0'


number = '1101'
from_base = 10
to_base = 2

converted_number = convert_base(number, from_base, to_base)
print(converted_number)











