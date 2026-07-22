from ultralytics import YOLO
result=YOLO("yolov8n.pt").predict(source='0',show=True)




'''
对上面代码的改进:

import os
import cv2
from ultralytics import YOLO
from aip import AipOcr
from dotenv import load_dotenv

# ================= 1. 读取 .env 配置文件 =================
# 获取当前脚本所在的绝对路径，确保无论你在哪个终端目录运行，都能找到 .env
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')
load_dotenv(env_path)

# 从环境变量中读取百度的配置
APP_ID = os.getenv('BAIDU_APP_ID')
API_KEY = os.getenv('BAIDU_API_KEY')
SECRET_KEY = os.getenv('BAIDU_SECRET_KEY')

# 验证是否读取成功
if not APP_ID or not API_KEY or not SECRET_KEY:
    print("错误：读取 .env 文件失败！请检查文件路径，或者确认文件内是否已填写百度 ID 和 Key。")
    exit()

# 初始化百度 OCR 客户端
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# ================= 2. 初始化 YOLO 和摄像头 =================
model = YOLO("yolov8n.pt")  # 加载模型
cap = cv2.VideoCapture(0)   # 打开默认摄像头（如果打不开，尝试把 0 改成 1）

if not cap.isOpened():
    print("错误：无法打开摄像头！请检查电脑摄像头是否被占用或禁用。")
    exit()

frame_count = 0  # 帧数计数器
ocr_text = ""    # 存储上次识别的 OCR 结果
paused = False   # 暂停状态标志（True为暂停，False为运行）
annotated_frame = None  # 用于保持当前要显示的画面

print("开始视频流检测...")
print("操作提示：按 空格键 暂停/继续画面，按 q 键 彻底退出程序。")

# ================= 3. 主循环 =================
while True:
    # --- 如果没有暂停，才读取画面并进行计算 ---
    if not paused:
        ret, frame = cap.read()
        if not ret:
            print("摄像头读取中断，程序自动结束。")
            break

        frame_count += 1
        
        # 1. 运行 YOLO 目标检测
        results = model(frame)
        annotated_frame = results[0].plot()  # 在画面上画检测框

        # 2. 每隔 10 帧调用一次百度 OCR (节省 API 调用次数)
        if frame_count % 10 == 0:
            try:
                # 将 OpenCV 的图像转换为二进制数据发给百度
                _, buffer = cv2.imencode('.jpg', frame)
                image_bytes = buffer.tobytes()

                # 调用百度 OCR 识别
                ocr_result = client.basicGeneral(image_bytes)

                # 解析返回的 JSON 结果
                if 'words_result' in ocr_result:
                    words_list = [item['words'] for item in ocr_result['words_result']]
                    ocr_text = " | ".join(words_list[:3])  # 提取并拼接前 3 行文字
                else:
                    ocr_text = "未识别到文字"
            except Exception as e:
                ocr_text = f"OCR 接口调用失败: {e}"

        # 3. 把 OCR 文字写在画面左上角
        if ocr_text and annotated_frame is not None:
            cv2.putText(annotated_frame, f"OCR: {ocr_text}", (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # --- 显示画面（不管是暂停还是运行，都要保持在窗口里） ---
    if annotated_frame is not None:
        cv2.imshow("YOLO + OCR", annotated_frame)

    # --- 监听键盘事件 ---
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):        # 按 q 键彻底退出
        print("正在退出程序...")
        break
    elif key == ord(' '):      # 按 空格键 切换暂停/继续
        paused = not paused
        if paused:
            print("画面已暂停，再按一次 空格键 继续运行...")
        else:
            print("恢复运行！")

# ================= 4. 释放资源 =================
cap.release()
cv2.destroyAllWindows()
'''