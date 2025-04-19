def number_to_chinese(num):
    chinese_numerals = {
        0: "零", 1: "一", 2: "二", 3: "三", 4: "四", 
        5: "五", 6: "六", 7: "七", 8: "八", 9: "九"
    }
    units = ["", "十", "百", "千"]
    
    if num == 0:
        return chinese_numerals[0]
    
    result = ""
    str_num = str(num)
    length = len(str_num)
    
    zero_flag = False  # Flag to avoid consecutive zeros
    
    for i, digit in enumerate(str_num):
        n = int(digit)
        if n != 0:
            if zero_flag:
                result += chinese_numerals[0]
                zero_flag = False
            result += chinese_numerals[n] + units[length - i - 1]
        else:
            zero_flag = True
    
    # Handle special cases like 10, 20, 30... where "一十" should just be "十"
    result = result.replace("一十", "十")
    
    return result

# Test cases
for num in [0, 3, 10, 15, 20, 30, 100, 105, 110, 2345, 9999]:
    print(f"{num}: {number_to_chinese(num)}")