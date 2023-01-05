# Calculate expense sum for two lists without function
#计算两个没有函数的列表的费用总和
chart_expenses = [20,30,45]
classification_expenses = [45,67,34]

total=0
for item in chart_expenses:
    total+=item
print("Total 图表总计:",total)

total=0
for item in classification_expenses:
    total+=item
print("Total 分类总计:",total)

# Calculate expense sum for two lists by using a function
def find_total(exp):
    '''
    This function takes list of numbers as input and returns sum of that list
    :param exp: input list
    :return: total sum
    '''
    total=0
    for item in exp:
        total+=item
    return total

_total=find_total(chart_expenses)
print("Total 总计:",_total)

_total=find_total(classification_expenses)
print("Total 分类总计:",_total)

# Explain argument, return value, function body with visuals

# documentation strings
print(help(find_total))

# Positional argument vs named arguments
def cylinder_volume(radius,height=1):
    print("radius is:",radius)
    print("height is:",height)
    area = 3.14*(radius**2)*height
    return area

r=5
h=10
print(cylinder_volume(height=h,radius=r))

# default arguments
r=5
h=10
print(cylinder_volume(radius=r))

# global vs local variables
