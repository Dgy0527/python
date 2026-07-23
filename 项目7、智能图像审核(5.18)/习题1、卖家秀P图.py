'''
1、PIL库:对图像进行处理的库,可以对图像进行切片、旋转、滤镜、输出文字、调色板等
2、image子模块:对图像进行基础操作的功能(open打开图像、show显示图像、save保存图像、paste粘贴图像)
3、imageDraw子模块:对图像的简单2D绘制功能,在图像上画直线、写文本
4、imageFont子模块:对图像写文本时,所涉及文本的字体、字号的设置
'''

from PIL import Image,ImageDraw,ImageFont
im1=Image.open('shoe.jpg') #打开图像'shoe.jpg'文件并赋值给im1
im2=Image.open('Nike.jpg') #打开图像'Nike.jpg'文件并赋值给im2
ziti=ImageFont.truetype(r'C:\Windows\Fonts\SIMYOU.TTF',60) #设置文本字体和字号
im1.paste(im2,(0,0)) #把im2图片复制到im1图片上
quyu=ImageDraw.Draw(im1) #在im1上留出一块区域
quyu.text((0,0),'卖家秀',fill='red',font=ziti) #在im1上写文本
im1.show() #显示图片
im1.save('new.jpg') #保存图片



'''
对上面代码的改进:

from PIL import Image, ImageDraw, ImageFont

# 1. 打开图片并统一转为 RGBA 模式（方便处理透明度）
im1 = Image.open('shoe.jpg').convert('RGBA')
im2 = Image.open('Nike.jpg').convert('RGBA')

# ================= 解决【白色方块】的核心步骤 =================
# 2. 去除 Nike 图片的白色背景，把白底变成透明
datas = im2.getdata()
new_data = []
for item in datas:
    # 只要像素接近白色(RGB值都大于240),就把它变成完全透明
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
im2.putdata(new_data)

# ================= 限制大小，防止把 Logo 撑得太大 =================
# 3. 把 Logo 的宽度限制在 180 像素左右，高度自动比例缩放
max_width = 180
w_percent = max_width / im2.width
new_h = int(im2.height * w_percent)
im2 = im2.resize((max_width, new_h), Image.Resampling.LANCZOS)

# ================= 绘制红色文字和贴上 Logo =================
# 4. 加载字体（你用到的 SIMYOU.TTF 是楷体），写红色文字
try:
    font = ImageFont.truetype(r'C:\Windows\Fonts\SIMYOU.TTF', 60)
except:
    font = ImageFont.load_default() # 如果系统没找到该字体，回退到默认

draw = ImageDraw.Draw(im1)
text_content = '卖家秀'
text_x, text_y = 30, 30  # 文字左上角坐标

# 写红字
draw.text((text_x, text_y), text_content, fill='red', font=font)

# 5. 获取文字的高度，把 Logo 贴在文字正下方
# 计算文字的包围盒
bbox = draw.textbbox((text_x, text_y), text_content, font=font)
text_height = bbox[3] - bbox[1] + 15 # 文字高度 + 15像素的间距

# 计算 Logo 粘贴的位置（左对齐，紧挨着文字下方）
logo_pos = (text_x, text_y + text_height)

# 使用 Mask 参数进行粘贴，完美去除透明背景的边缘
im1.paste(im2, logo_pos, mask=im2)

# ================= 保存效果图 =================
# 预览
im1.show()
# 保存为新图片(JPG 不支持透明度，需要转换回 RGB)
im1.convert('RGB').save('new.jpg')
print("处理完成！文件已保存为 new.jpg")

'''