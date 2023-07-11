# ماشین کد زیر فقط برای R-format, I-format کار میکند
import random
opcode_dict = {'add d0,d1': '0000', 'add d0,d2': '0000', 'add d0,d3': '0000',
               'add d1,d0': '0000', 'add d1,d2': '0000', 'add d1,d3': '0000',
               'add d2,d0': '0000', 'add d2,d1': '0000', 'add d2,d3': '0000',
               'add d3,d0': '0000', 'add d3,d1': '0000', 'add d3,d2': '0000',
               'sub d0,d1': '0010', 'sub d0,d2': '0010', 'sub d0,d3': '0010',
               'sub d1,d0': '0010', 'sub d1,d2': '0010', 'sub d1,d3': '0010',
               'sub d2,d0': '0010', 'sub d2,d1': '0010', 'sub d2,d3': '0010',
               'sub d3,d0': '0010', 'sub d3,d1': '0010', 'sub d3,d2': '0010',
               'and d0,d1': '0101', 'and d0,d2': '0101', 'and d0,d3': '0101',
               'and d1,d0': '0101', 'and d1,d2': '0101', 'and d1,d3': '0101',
               'and d2,d0': '0101', 'and d2,d1': '0101', 'and d2,d3': '0101',
               'and d3,d0': '0101', 'and d3,d1': '0101', 'and d3,d2': '0101',
               'cmp d0,d1': '1101', 'cmp d0,d2': '1101', 'cmp d0,d3': '1101',
               'cmp d1,d0': '1101', 'cmp d1,d2': '1101', 'cmp d1,d3': '1101',
               'cmp d2,d0': '1101', 'cmp d2,d1': '1101', 'cmp d2,d3': '1101',
               'cmp d3,d0': '1101', 'cmp d3,d1': '1101', 'cmp d3,d2': '1101',
               'clr d0': '1011', 'clr d1': '1011', 'clr d2': '1011', 'clr d3': '1011',
               }


def get_opcode(command):
    if command.startswith('add d0,') or command.startswith('add d1,') \
            or command.startswith('add d2,') or command.startswith('add d3,'):
        parts = command.split(',')
        if len(parts) == 2 and parts[1].isdigit():
            return '0001'
    elif command.startswith('addi d0,') or command.startswith('addi d1,') \
            or command.startswith('addi d2,') or command.startswith('addi d3,'):
        parts = command.split(',')
        if len(parts) == 2 and parts[1].isdigit():
            return '0011'
    elif command.startswith('sll d0,') or command.startswith('sll d1,') \
            or command.startswith('sll d2,') or command.startswith('sll d3,'):
        parts = command.split(',')
        if len(parts) == 2 and parts[1].isdigit():
            return '0110'
    elif command.startswith('lw d0,') or command.startswith('lw d1,') \
            or command.startswith('lw d2,') or command.startswith('lw d3,'):
        parts = command.split(',')
        if len(parts) == 2 and parts[1].isdigit():
            return '0111'
    elif command.startswith('sw d0,') or command.startswith('sw d1,') \
            or command.startswith('sw d2,') or command.startswith('sw d3,'):
        parts = command.split(',')
        if len(parts) == 2 and parts[1].isdigit():
            return '1001'
    elif command.startswith('mov ba,'):
        parts = command.split(',')
        if len(parts) == 2 and parts[1].isdigit():
            return '1100'
    elif command.startswith('bne '):
        parts = command.split(' ')
        if len(parts) == 2 and parts[1].isdigit():
            return '1110'
    elif command.startswith('jmp '):
        parts = command.split(' ')
        if len(parts) == 2 and parts[1].isdigit():
            return '1111'
    return opcode_dict.get(command, 'Invalid command')


command = input('Enter the command: ')


def split_string(command):
    # پیدا کردن اولین اسپیس در رشته
    first_space_index = command.find(' ')
    # پیدا کردن اولین کاما در رشته
    first_comma_index = command.find(',')

    # جدا کردن قسمت‌های مختلف رشته
    x = command[:first_space_index]
    key1 = command[first_space_index + 1:first_comma_index]
    key2 = command[first_comma_index + 1:]

    # بررسی و تبدیل key2 به مبنای دو اگر شامل اعداد بود
    if key2.isdigit():
        binary_key2 = bin(int(key2))[2:].zfill(8)
        key2 = binary_key2

    # برگرداندن متغیرهای جداگانه
    return x, key1, key2


x, key1, key2 = split_string(command)
opcode = get_opcode(command)
# print(opcode)


reg_dict = {'$0': 0, 'd0': 1, 'd1': 2, 'd2': 3, 'd3': 4,
            'a0': 5, 'a1': 6, 'a2': 7, 'a3': 8,
            'sr': 9, 'ba': 10, 'pc': 11
            }


value = reg_dict.get(key1)  # دریافت مقدار متناظر با کلید ورودی
if value is not None:
    bin_value = bin(value)[2:].zfill(4)
    rd = bin_value
    # print(rd)
# else:
    # در صورتی که کلید ورودی معتبر نباشد، پیام خطای مناسب چاپ می‌شود
    # print('Invalid input')


# command3 = input('Enter the rs: ')
value = reg_dict.get(key2)
if key2.isdigit():
    binary_key2 = bin(int(key2))[2:].zfill(8)
    rs = binary_key2
else:
    value = reg_dict.get(key2)  # دریافت مقدار متناظر با کلید ورودی
    if value is not None:
        bin_value = bin(value)[2:].zfill(4)
        rs = bin_value
#     print(rs)
# else:
#     # در صورتی که کلید ورودی معتبر نباشد، پیام خطای مناسب چاپ می‌شود
#     print('Invalid input')

if len(rs) == 4:
    nop = bin(random.randint(0, 15))[2:].zfill(4)
else:
    nop = ""
if nop == "":
    concatenated = str(opcode) + str(rd) + str(key2)
else:
    concatenated = str(opcode) + str(rd) + str(rs) + str(nop)
print("machine code is: " + concatenated)
