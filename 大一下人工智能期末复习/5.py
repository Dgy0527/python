'''
5、题目简述

人脸识别,是基于人的脸部特征信息进行身份识别的一种生物识别技术。
用摄像机或摄像头采集含有人脸的图像或视频流,并自动在图像中检测和跟踪人脸,进而对检测到的人脸进行脸部识别的一系列相关技术。
对上图的人脸识别,得到下图data的关键数据。
现在要基于data的数据,统计某个性别的人数、平均年龄(保留2为小数)。

data = {'face_num':5,
  'face_list':[{ "token":87091,"age":26,"gender":"女","beauty":78.55 },
               { "token":35235,"age":37,"gender":"女","beauty":83.18 },
               { "token":69024,"age":28,"gender":"男","beauty":65.03 },
               { "token":50627,"age":41,"gender":"男","beauty":71.40 },
               { "token":19183,"age":29,"gender":"女","beauty":59.26 }
             ]
}

程序说明
1.输入性别（男/女）
2.输出此性别人数、平均年龄,平均年龄要保留2位小数
注：计算公式：平均年龄=年龄总和/人数

样例输入
请输入性别（男/女）：女
样例输出
此性别人数： 3
平均年龄为： 30.67

'''

#参考答案
data = {'face_num':5,
     'face_list':[{ "token":87091,"age":26,"gender":"女","beauty":78.55 },
               { "token":35235,"age":37,"gender":"女","beauty":83.18 },
               { "token":69024,"age":28,"gender":"男","beauty":65.03 },
               { "token":50627,"age":41,"gender":"男","beauty":71.40 },
              { "token":19183,"age":29,"gender":"女","beauty":59.26 }
              ]
      }
sex=input('请输入性别(男/女):')

n=0;s=0
for face in data['face_list']:
    if face["gender"]==sex:
        n=n+1
        s=s+face["age"]

print("此性别人数:",n)
print("平均年龄为:",round(s/n,2))

'''
对上面代码的改进:

data = {
    'face_num': 5,
    'face_list': [
        {"token": 87091, "age": 26, "gender": "女", "beauty": 78.55},
        {"token": 35235, "age": 37, "gender": "女", "beauty": 83.18},
        {"token": 69024, "age": 28, "gender": "男", "beauty": 65.03},
        {"token": 50627, "age": 41, "gender": "男", "beauty": 71.40},
        {"token": 19183, "age": 29, "gender": "女", "beauty": 59.26}
    ]
}

# 1. 增加输入验证循环，并去除首尾空格
while True:
    sex = input('请输入性别（男/女）：').strip()
    if sex in ['男', '女']:
        break
    print('输入错误，请重新输入男或女！')

count = 0
total_age = 0

# 2. 遍历并统计
for face in data['face_list']:
    if face["gender"] == sex:
        count += 1
        total_age += face["age"]

# 3. 防止除以0的错误，并使用更精确的格式化输出
if count > 0:
    avg_age = total_age / count
    print("此性别人数：", count)
    print(f"平均年龄为： {avg_age:.2f}")  # 使用 f-string 格式化保留两位小数
else:
    print("此性别人数： 0")
    print("平均年龄为： 0.00")
'''