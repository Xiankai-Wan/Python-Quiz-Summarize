# 练习：创建帮助函数 convert_to_numeric
# 这个时候可以填写帮助函数的正文了。
#
# 在该练习中，完成 convert_to_numeric() 函数。此函数的输入可以是字符串、整数或浮点数。"3"、3 以及 3.0 都是有效的输入。该函数应该返回一个浮点数。
#
# 确保通过调用函数和打印输出，也可以是输出类型来测试该函数。从上一个练习开始你自己或我们的框架。
def convert_to_numeric(score):
    """Turn the score to float
    """
    numeric = float(score)
    return numeric

print(convert_to_numeric(3))
