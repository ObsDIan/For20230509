import os
import csv

def CSVReader (path, new_path):
    new = []
    # 讀取CSV檔案
    with open(path, newline='', encoding='utf-8') as r:
        rows = csv.reader(r)
        # 取出第一列為標題
        header = next(rows)
        header.append('index')
        # 取出每一列
        for row in rows:
            question = row[0]
            ans = row[1]
            # 為每一列創建一個新的欄位['index']內容為問題與答案的結合
            row.append(question + ' ' + ans)
            # 將新的列加入新的列表
            new.append(row)
    # 將新的標題與每一列寫入CSV
    with open(new_path, 'w', newline='', encoding='utf-8') as w:
        writer = csv.writer(w)
        writer.writerow(header)
        writer.writerows(new)
    return new