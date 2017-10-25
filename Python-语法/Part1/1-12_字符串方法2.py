# 练习：使用字符串格式简化代码
# 本练习中的代码可生成天气报告警报。之前的程序员使用字符串连接来组合警报，这会导致一些代码难以阅读。使用 format 方法重写代码。新代码可产生与所替换旧代码相同的字符串。
city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"

#todo rewrite this line to use the format method rather than string concatenation
#alert = "Today's forecast for " + city + ": The temperature will range from " + str(low_temperature) + " to " + str(high_temperature) + " " + temperature_unit + ". Conditions will be " + weather_conditions + "."
alert ="Today's forecast for {}: The temperature will range from {} to {} {}. Conditions will be {}.".format(city,str(low_temperature),str(high_temperature),temperature_unit,weather_conditions)
# print the alert
print(alert)
