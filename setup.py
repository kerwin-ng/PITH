# Version: 0.15
# Date: 2022/07/16

import os
import time
from configparser import ConfigParser
from PIL import Image, ImageDraw, ImageFont


def read_config(config_path):
    cfg = ConfigParser()
    cfg.read(config_path)

    tbp = cfg.get('path', 'tbp')
    save = cfg.get('path', 'save')
    width = cfg.get('img', 'width')
    height = cfg.get('img', 'height')
    time_text = cfg.get('img', 'time_text')
    location_text = cfg.get('img', 'location_text')
    font_size = cfg.get('img', 'font_size')
    save_file_name = cfg.get('img', 'save_file_name')

    # 转化数据类型
    width = float(width)
    height = float(height)
    font_size = int(font_size)

    return tbp, save, width, height, time_text, location_text, font_size, save_file_name


def img_process(tbp, save, width, height, time_text, location_text, font_size, save_file_name):
    counter = 0

    for root, ds, fs in os.walk(tbp):
        for f in fs:
            fullname = os.path.join(root, f)
            print('正在处理: [{}]'.format(fullname))
            image = Image.open(fullname)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(r'./yahei.ttf', font_size)
            img_width = int(image.width - 20)
            img_height = int(image.height - 20)
            draw.text((20, 20), time_text + '\n' + location_text, font=font, align='left')
            # draw.text((img_height, img_width), '今日水印\n相机\n真实时间', font=font, align='center')
            image.save(save + '/' + save_file_name + f)
            counter = counter + 1
            print('[{}]: [{}] 已完成 \n'.format(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()), fullname))

    return counter


def main(cfg_path):
    tbp, save, width, height, time_text, location_text, font_size, save_file_name, \
        = read_config(cfg_path)
    print('Version: 0.11 0712\n源文件目录: {}\n保存目录: {}'.format(tbp, save))
    print('字号设置: {}\n'.format(font_size))
    counter = img_process(tbp, save, width, height, time_text, location_text,
                          font_size, save_file_name)

    print('共处理 {} 张照片'.format(counter))


config_path = './config.ini'  # 配置文件位置
main(config_path)
