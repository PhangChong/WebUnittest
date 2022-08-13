import csv


# 设计函数专门读取 csv文件
def get_csv_data(csv_file, line):
    csv_file = open(csv_file, 'r', encoding='utf-8')
    reader = csv.reader(csv_file)
    # 参数2 :决定了下标位置的开始计数方式
    for index, row in enumerate(reader, 1):
        if index == line:
            # print(row)
            return row


if __name__ == "__main__":
    get_csv_data("../testData/re_login.csv", 1)
    get_csv_data("../testData/re_login.csv", 2)
    get_csv_data("../testData/re_login.csv", 3)
