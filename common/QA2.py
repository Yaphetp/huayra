# coding= utf-8
'''
1、python语句一般以新行作为语句的结束。代码编写换行使用 \，如果有{} () [] ,则无需刻意换行（直接换）。
注意：如果输出结果需要换行，代码编写使用 '\n'

2、同一行编写多条语句，使用;隔开
注意：区分同一条语句多个值的展示不同。 print a,b,c; print a,b,c
3、指数表达 **
4、存在运算符 >= <=

5、name 定位，就是指 text； 而class_name一般指 class

6、双元素定位  解决：通过if id('xxx').text() == ‘hi’，目前我是这样理解的。
7、编码问题 
 GBK(GB2312)
 UTF-8（unicode是所有环境都支持的编码格式）
 ASCII
 
在开发Python程序的过程中，会涉及到三个方面的编码：
Python程序文件的编码 ：文件本身的编码，coding=utf-8即可支持中文输入。
Python程序运行时环境（IDE）的编码, windows系统的默认编码格式。 
    如果py文件与程序运行环境（windows）不一致，需要解码- 重新编码为程序运行环境编码格式。
Python程序读取外部文件、网页的编码
 

问题：u‘’ 
解决：windows编码方法（GBK）与python文件保存时的编码方式不一样。运行解码时(使用windows操作系统)，使用GBK解码utf-8，出现乱码。
print u'是' #方法1
print '是'.decode("gbk") #方法2

isinstance(s,unicode):判断s是否是unicode编码，如果是就返回true,否则返回false*
    -- 注意unicode是一种数据类型，不是编码格式。
type(s):判断数据类型
chardet.detect(s)：概率判断编码格式
8、
问题：两层判断的处理：1）首先滑动寻找第一个条件（1月4日）的数据出现；2）判断第二个条件（1月4日的数据是否可预约，循环滑动寻找）
解决：1：while第一次循环 ；2：while第二次循环，内置break if语句

9、此方法时将python的默认ascii码改为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

10、
编码：真实字符与二进制串的对应关系，真实字符（unicode）→二进制str串
解码：二进制串与真实字符的对应关系，二进制str串→真实字符
在python中，编码解码其实是不同编码系统间的转换，默认情况下，转换目标是Unicode，
即编码unicode→str，解码str→unicode，其中str指的是字节流
https://www.cnblogs.com/shine-lee/p/4504559.html

11、 in range (start, end),默认步长是+1；所以end必须 > start; 如果想start > end（比如排序时），可步长 设定为 -1

12、使用in range时注意下标越界，以及len的值。
1）in range(start, end)是不包括end的值的。
2）len的值是end-start。
3) 下标是从[0, end-start-1]

13、 keyevent：https://www.cnblogs.com/harry-xiaojun/p/6900259.html

14、魅蓝5测试，搜索键实际keycode值是66，并非88.所有有时，这两个键盘的keycode设定需要变通，因为不是确定的。

15、sendkeys 英文输入不完整？？ 包括之前使用 123abc@的时候，@显示数字2
    解决：使用self.driver.hide_keyboard()方法解决。全局控制方式：resetKeyboard=True
    sendkeys 中文无法输入？？
    解决：unicodeKeyboard=True
14、清除输入内容???
说明：目前碰到的editText，通过send_keys方法都可以自动选中被替换掉，不需要额外的clear方法。
以后如果有特殊情况，碰到再说。

15、import时尽量完整引入（路径的完整性）

16、adb 命令
-- adb shell wm size  获取分辨率

17、os.walk（目录，topdown=）产生三元组tuple，可通过for循环进行遍历------（参数指定的目录、遍历目录下的文件夹、遍历目录下的文件）/
    如果 topdown=False，则从最下层的文件夹（目录）开始遍历。
    
18、判断是文件还是文件夹，注意：path必须带文件or文件夹名称。
os.path.isfile(path) 
os.path.isdir(path)

19、位运算，数字看做二进制进行计算
按位与：&  有0为0
按位或：|  有1为1
按位异或： ^ 相异为1，相同为0
按位取反：~
按位左移：a << 2,箭头方向, 左边长出去的砍掉2未，右边空出的2位补0
按位右移：a >> 2, 箭头方向右移，右边长出去的二进制砍掉2位，左边空出来的2位补充0


20、汉明距离（hammingDistance）
方法1：
b1 = 100
b2 = 1
print bin(b1 ^ b2).count('1')
如果使用该方法求汉明距离，b1为int，b2为int；所以如果/
b1 和 b2 为两张图片，如何将图片转换为2进制- 10进制int。


21、2进制、8进制、16进制转换为10进制
x = int（‘1010’， base=2、8、16），注意第一个参数为str

binascii模块下（b2a_hex(), hexlify()）: b2a_hex('huayra')
实际就是 str -》 16进制

函数hexlify和b2a_hex实际是一个函数，建议使用hexlify。
作用是返回的二进制数据的十六进制表示。每一个字节的数据转换成相应的2位十六进制表示。
因此产生的字串是源数据两倍长度。a2b_hex和unhexlify则执行反向操作。

22、图像识别
http://www.jb51.net/article/83315.htm
1） 先识别图像的特征，然后再相比
2） 计算机很容易识别到图像的像素值
3） 因此，在图像识别中，颜色特征是最为常用的
4） 其余常用的特征还有纹理特征、形状特征和空间关系特征等
5） 其中又分为
直方图
颜色集
颜色矩
聚合向量
相关图

matplotlib、PIL、cv2图像操作

23、opencv相关函数
1) cv2.resize(cv2.imread(url), (256, 256))  按指定大小缩放

获取直方图数据（通过灰度图）
2) hist = cv2.calcHist([image],  
    [0], #使用的通道  
    None, #没有使用mask  
    [256], #HistSize（直方柱） 
    [0.0,255.0]) #直方图柱的范围（0-256的像素）  
    返回矩阵
    [[ 3644.]
 [ 2273.]]
3) cv2.minMaxLoc(hist) 寻找矩阵中最小值、最大值及其位置
(0.0, 6157.0, (0, 255), (0, 213))

4) numpy as np.
    np.zeros(shape, dtype= ), np.zeros(5, int); np.zeros([2,3], uint8)
    返回给定形状、类型的0填充的数组
    # 创建用于创建直方图的全0图像
    [0 0 0 0 0]
    
如下代码可以实现，将普通图片-》 cv2(opencv库)直方图
img_read = cv2.imread(r'C:\Users\wangping\Desktop\spring.png', 1)
img_size = cv2.resize(img_read, (640, 430))
img_hist = cv2.calcHist([img_read], [0], None, [256], [0.00, 255.00])
minval, maxval, minLoc, maxLoc = cv2.minMaxLoc(img_hist)
img_shape = np.zeros([256, 256, 3], np.uint8)
hpt = int (0.9 * 256)

for h in range(256):
    intensity = int (img_hist[h] * hpt / maxval)
    cv2.line(img_shape, (h, 256), (h, 256-intensity), [255, 255, 255])
    
cv2.imshow('img_shape', img_shape)
cv2.waitKey(10000)
cv2.destroyAllWindows()

使用matplotlib库绘图
matplotlib.pyplot 
pyplot.plot()
pyplot.show()

(B,G,R) = cv2.split(img_size)
split方法只可以分解为这三个单通道

# 获取图像的行数（高），列数（宽）,单位像素
img.shape[0], img.shape[1]
# 使用 image[img.shape[0], img.shape[1]]获取图像的RGB值

# 获取每一列的均值
np.mean(img)
'''