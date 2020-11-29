import os 
import re
from PIL import Image

# 读取标签
def read_tagers(path="./tagers.txt"):
    with open(path) as rf:
        text = rf.read()
        words = re.split(r"\n+", text)
        words = [word.strip() for word in words if word.strip()]
        print("tagers = {}".format(len(words)))
        return words

Tagers = read_tagers()
num = 0
# 切割图片
def splitimage(src, rownum, colnum, dstpath):
    global num
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('བཅད་པའི་རི་མོ།')
        ext = "png" #re.findall(r"\.([^\.]+)$",src)[-1]# png jpg
        rowheight = 112 #y
        colwidth = 114 #x
        start_x = 70
        start_y = 82
        for r in range(rownum):
            for c in range(colnum):
                box = (start_x+c * colwidth, start_y+r * rowheight,
                       start_x+(c + 1) * colwidth, start_y+(r + 1) * rowheight)
                img.crop(box).resize((72,72)).save(os.path.join(dstpath, Tagers[num] + '_' +"1" + '.' + ext))
                num = num + 1
        print('ཁྱོན་བསྡོམས་རི་མོ་ཆུང་བ། %s གཅོད་ཐུབ་སོང་།' % num)
    else:
        print('ནོར་འཛོལ་བྱུང་བ།')

# 创建文件夹
def mkdir(path="./outputs/"):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        os.makedirs(path)
        print (path+' གསར་འཛུགས་བྱས་པ།')
        return True
    else:
        print (path + ' དཀར་ཆག་སྔར་ནས་ཡོད་ཟིན་པ་རེད།')
        return False

folder = r"/home/samdrub/Desktop/Data-code/dataset-2020.6.7/wujian/Monotype Corsiva/2" # 存放图片的文件夹
t = 23
h = ".png"
paths = [str(i)+h for i in range(1,t+1)]#os.listdir(folder)
#paths = sorted(paths) # 排序
print(paths)
paths = [os.path.join(folder,path) for path in paths]

output_path = "./outputs/"
mkdir(output_path)
row, col = 6,4
for path in paths: # 批量操作
        print(path)
        # 调用函数
        splitimage(path, row, col, output_path)
