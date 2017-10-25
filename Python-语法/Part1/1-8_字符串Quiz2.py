# 练习：编写服务器日志消息
# 在该编程练习中，大家将使用关于字符串的所学内容编写服务器日志消息。
#
# 我们将为大家提供用户的示例数据、访问时间和访问的网站。你们应该使用所提供的变量和所学技术打印如下所示的日志消息（用相应变量的值替换用户名、url 和时间戳）：
#
# Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.
#
# 编码时，使用“测试答案”按钮查看结果。

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message incorporating the strings above.
# The message should be use the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + " accessed the site " + url + " at " + timestamp + ".")
