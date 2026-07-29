canteen = [
    {
        'dname': '南门食堂',
        'seats': 760,
        'kol_dish': ['汤粉', '排骨串', '烫菜'],
        'stars': '四星',
        'manager': '李主管'
    },
    {
        'dname': '北区食堂',
        'seats': 676,
        'kol_dish': ['多味屋', '五香鱼粉', '牛腩粉', '瓦罐汤'],
        'stars': '五星',
        'manager': '王主管'
    },
    {
        'dname': '教工食堂',
        'seats': 1200,
        'kol_dish': ['小炒', '麻辣烫', '酸菜鱼', '牛肉面'],
        'stars': '三星',
        'manager': '张主管'
    },
    {
        'dname': '柳园餐厅',
        'seats': 1910,
        'kol_dish': ['扒虾', '木桶饭', '鸡扒饭', '云吞', '焖菜'],
        'stars': '四星',
        'manager': '罗主管'
    },
    {
        'dname': '锦园学生餐厅',
        'seats': 3250,
        'kol_dish': ['牛杂', '机器人刀削面', '饭煲', '饺子'],
        'stars': '五星',
        'manager': '贺主管'
    },
    {
        'dname': '民族风味餐厅',
        'seats': 120,
        'kol_dish': ['大盘鸡', '兰州拉面', '烤馕', '新疆拌面'],
        'stars': '五星',
        'manager': '买买提主管'
    }
]

dish_name=input('请输入你想吃的菜名:')
flag=False
for item in canteen:
    if dish_name in item['kol_dish']:
        print('欢迎来',item['dname'],'品尝',dish_name)
        flag=True
if not flag:
    print('没有找到你想吃的菜名。')



'''
对上面代码的改进:

def find_canteens_by_dish(dish_name, canteen_list):
    """返回所有包含该菜名的食堂名称列表"""
    dish_name = dish_name.strip()
    if not dish_name:
        return []
    found = []
    for item in canteen_list:
        # 若想支持部分匹配，可改为 any(dish_name in dish for dish in item['kol_dish'])
        if dish_name in item['kol_dish']:
            found.append(item['dname'])
    return found

dish = input('请输入你想吃的菜名:').strip()
matched = find_canteens_by_dish(dish, canteen)

if matched:
    # 合并输出
    names = '、'.join(matched)
    print(f'欢迎来 {names} 品尝 {dish}')
else:
    print('没有找到你想吃的菜名。')

'''