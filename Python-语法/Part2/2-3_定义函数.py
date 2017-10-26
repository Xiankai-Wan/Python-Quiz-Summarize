# 练习：readable_timedelta
# 编写一个名为 readable_timedelta 的函数。该函数接收一个参数（一个整数型变量 days），返回一个字符串，表示传入的天数有几星期零几天。例如，readable_timedelta(10) 应返回 1 week(s) and 3 day(s)。
#
# 编写时请加上一个 docstring，用于说明该函数的目的。
# -*- coding: UTF-8 -*-
# Write your code for readable_timedelta here.
def readable_timedelta(days):
    """Return how mang weeks and days
    """
    week = str(days/7)
    day = str(days%7)
    return "{} week(s) and {} day(s)".format(week,day)

# Uncomment this function call to test it:
print(readable_timedelta(10))
#readable_timedelta(10)
