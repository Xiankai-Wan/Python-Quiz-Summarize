# 测验：列表索引
# 完成函数 how_many_days，其将输入一个表示月份的数字，并返回该月份的天数。我们定义的 days_in_month 函数是表示每个月有多少天的列表。例如，days_in_month(8) 应该返回 31，因为第八个月，即八月，有 31 天。
#
# 记住索引要从零开始！
#
# def how_many_days(month_number):
#     """Returns the number of days in a month.
#     WARNING: This function doesn't account for leap years!
#     """
#     days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
#     #todo: return the correct value
#     return days_in_month[month_number - 1]
#
# # This test case should print 31, the number of days in the eighth month, August
# print(how_many_days(8))

def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    return days_in_month[month_number - 1]

# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8))
