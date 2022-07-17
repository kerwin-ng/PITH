# Version: 0.2
# Date: 2022/07/16

import csv
import os


def config_csv(csv_path, tbp):
    header = ['path', 'name', 'time_text', 'location_text']
    with open(csv_path, 'w+', encoding='utf-8-sig', newline='') as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(header)
        for root, ds, fs in os.walk(tbp):
            for f in fs:
                path = os.path.join(root, f)
                data = (path, f, '', '', '')
                print('正在写入[{}]' .format(data))
                writer.writerow(data)

        print('Done')

    return


def csv_read(csv_path):
    with open(csv_path, 'r', encoding='utf-8-sig') as file_obj:
        reader = csv.reader(file_obj)
        for r in reader:
            print(r)

    return


config_csv('./config.csv', './tbp')
# csv_read('./config.csv')
