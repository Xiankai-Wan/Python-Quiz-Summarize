# 练习：销售总额
# 在该练习中，你需要更改输入和输出数据的类型来获得最终结果。
#
# 根据提供的数据计算并打印一周的销售总额。打印一个格式为："This week's total sales: xxx" 的字符串，其中 xxx 将是实际销售总额的数字。大家需要更改输入数据的类型才可以计算销售总额。

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write several lines of code before the print statement.
total_sales = (int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales))
print("This week's total sales: " + str(total_sales))
