# 练习：里约热内卢或旧金山哪个人口更密集？
# 在该练习中尝试使用比较运算符！该代码计算了里约热内卢和旧金山的人口密度。
#
# 编写代码，比较这些密度。旧金山的人口比里约热内卢更密集吗？如果是，则打印 True，否则打印 False。

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
