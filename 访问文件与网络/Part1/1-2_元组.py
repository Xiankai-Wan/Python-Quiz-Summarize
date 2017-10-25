# 练习：天和小时
# 尝试编写一个使用元组返回多个值的函数。编写 hours2days 函数，传入一个整数类型的参数，该参数表示一个以小时为单位的时间段。该函数应该返回一个元组，用天和小时为单位表示传入的时间段，不足一天的时间用小时表示。例如，39 个小时表示 1 天 15 个小时，所以函数返回的应该是 (1,15)。
#
# 这些例子演示了该函数的使用：
# >>> hours2days(24) # 24 hours is one day and zero hours
# (1, 0)
# >>> hours2days(25) # 25 hours is one day and one hour
# (1, 1)
# >>> hours2days(10000)
# (416, 16)

def hours2days(input_hours):
    day = int(input_hours/24)
    hour = input_hours%24
    return day,hour

print(hours2days(24))
