"""
    把一个浮点数分解成整数部分和小数部分字符串
    num是需要被分解的浮点数
    返回分解出来的整数部分和小数部分
    第一个数组元素是整数部分，第二个数组元素是小数部分
"""


def divide(num):
    # 将一个浮点数强制类型转换为int类型，即得到它的整数部分
    integer = int(num)
    # 浮点数减去整数部分，得到小数部分，小数部分乘以100后再取整，得到2位小数
    fraction = round((num - integer) * 100)
    return str(integer), str(fraction)


han_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
unit_list = ["十", "百", "千"]
change_list = ["角", "分"]

"""
    把一个4位的数字字符串变成汉字字符串
    num_str是需要被转换的4位数字字符串
    返回4位数字字符串被转换成汉字字符串
"""


def four_to_hanstr(num_str):
    result = ""
    num_len = len(num_str)
    # 标志位，判零
    flag = False
    # 依次遍历数字字符串的每一位数字
    for i in range(num_len):
        # 把字符串转换成数值
        num = int(num_str[i])
        # 如果不是最后一位数字，而且数字不是零，则需要添加单位(千、百、十)
        if num != 0:
            if flag:
                result += "零"
                flag = False
            if i == num_len - 1:
                result += han_list[num]
            else:
                result += han_list[num] + unit_list[num_len - 2 - i]
        # 否则不用添加单位
        else:
            flag = True

    return result


"""
    把数字字符串变成汉字字符串
    num_str是需要被转换的数字字符串
    返回数字字符串被转换成汉字字符串
"""


def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12:
        print('数字太大，翻译不了')
        return
    # 如果大于8位，包含单位“亿”
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8]) + "亿" + \
               four_to_hanstr(num_str[-8: -4]) + "万" + \
               four_to_hanstr(num_str[-4:]) + "元"
    elif str_len > 4:
        return four_to_hanstr(num_str[: -4]) + "万" + \
               four_to_hanstr(num_str[-4:]) + "元"
    else:
        return four_to_hanstr(num_str) + "元"


# 小数点后的零钱转换
def change_to_str(num_str):
    count = 0
    result = ""
    if len(num_str) == 1:
        if num_str == '0':
            return result + "整"
        else:
            return result + han_list[int(num_str)] + "分"
    else:
        for i in num_str:
            if i == '0':
                continue
            result += han_list[int(i)] + change_list[count]
            count += 1
        return result


input_num = float(input("请输入一个浮点数： "))
# 测试把一个浮点数分解成整数部分和小数部分
integer, fraction = divide(input_num)
# 测试把一个4位的数字字符串变成汉字字符串
print(integer_to_str(integer), end="")
print(change_to_str(fraction))
