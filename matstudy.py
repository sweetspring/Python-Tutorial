import matplotlib.pyplot as plt #导入pyplot子库
#import numpy as np

plt.figure(figsize=(8, 4)) #创建一个绘图对象, 并设置对象的宽度和高度, 如果不创建直接调用plot, Matplotlib会直接创建一个绘图对象
plt.plot([1, 2, 3, 4]) #此处设置y的坐标为[1, 2, 3, 4], 则x的坐标默认为[0, 1, 2, 3]在绘图对象中进行绘图, 可以设置label, color和linewidth关键字参数
plt.ylabel('some numbers') #给y轴添加标签, 给x轴加标签用xlable
plt.title("hello"); #给2D图加标题
plt.show() #显示2D图


#import matplotlib.pyplot as plt 
x = [0, 1, 2, 4, 5, 6]
y = [1, 2, 3, 2, 4, 1]
plt.plot(x, y, '-*r') # 虚线, 星点, 红色
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#import numpy as np
#import matplotlib.pyplot as plt 
x = [0, 1, 2, 4, 5, 6]
y = [1, 2, 3, 2, 4, 1]
z = [1, 2, 3, 4, 5, 6]
plt.plot(x, y, '--*r', x, z, '-.+g')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("hello world")
plt.show()


#import numpy as np
#import matplotlib.pyplot as plt 
x = [0, 1, 2, 4, 5, 6]
y = [1, 2, 3, 2, 4, 1]
z = [1, 2, 3, 4, 5, 6]
plt.bar(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#import numpy as np
#import matplotlib.pyplot as plt 
x = [0, 1, 2, 4, 5, 6]
y = [1, 2, 3, 2, 4, 1]
z = [1, 2, 3, 4, 5, 6]
plt.figure(1)
plt.subplot(211)
plt.plot(x, y, '-+b')
plt.subplot(212)
plt.plot(x, z, '-.*r')
plt.show()
 
 
#import numpy as np
#import matplotlib.pyplot as plt 
x = [0, 1, 2, 4, 5, 6]
y = [1, 2, 3, 2, 4, 1]
plt.plot(x, y, '-.*r') 
plt.text(1, 2, "I'm a text") #前两个参数表示文本坐标, 第三个参数为要添加的文本
plt.show()
 
#import numpy as np
#import matplotlib.pyplot as plt 
line1, = plt.plot([1, 2, 3])
line2, = plt.plot([3, 2, 1], '--b')
plt.legend((line1, line2), ('line1', 'line2'))
plt.show()

