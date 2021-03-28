import sqlite3
import os


dir_name = "data"
file_name = "test.db"
file_path = f'{dir_name}/{file_name}'
os.makedirs(dir_name, exist_ok=True)

if os.path.exists(file_path):
    os.remove(file_path)

# SQLと接続
conn = sqlite3.connect(file_path) #パス指定の場合はローカルと接続。存在しない場合は自動的に作成。
curs = conn.cursor()

# テーブルを作成(テーブル名：persons)
table = "persons"
row1 = "name"
curs.execute(f'CREATE TABLE {table}(id INTEGER PRIMARY KEY AUTOINCREMENT, {row1} String)')

# テーブルに値を挿入する
curs.execute(f'INSERT INTO {table}({row1}) values("A")')
curs.execute(f'INSERT INTO {table}({row1}) values("B")')
curs.execute(f'INSERT INTO {table}({row1}) values("C")')
curs.execute(f'INSERT INTO {table}({row1}) values("D")')
#curs.execute('INSERT INTO {table}({row1}) values("E")')


# 値を更新する
curs.execute(f'UPDATE {table} SET {row1} = "DD" WHERE {row1} = "D"') #見つからなければ実行されない


# 値を消去する
curs.execute(f'DELETE FROM {table} WHERE {row1} = "DD"') #見つからなければ実行されない


# テーブルを表示する
curs.execute(f'SELECT * FROM {table};')
result = curs.fetchall()
print("全てのフィールド")
print(result)


#順列を表示
curs.execute(f'SELECT * FROM {table} p1 CROSS JOIN {table} p2 WHERE p1.{row1} <> p2.{row1};')
result = curs.fetchall()
print("順列総数:"+str(len(result)))
for item in result:
    p1, p2 = item[1], item[3]
    print(f"[{p1}, {p2}]")


#組み合わせを表示
curs.execute(f'SELECT * FROM {table} p1 CROSS JOIN {table} p2 WHERE p1.{row1} < p2.{row1};')
result = curs.fetchall()
print("組み合わせ総数:"+str(len(result)))
for item in result:
    p1, p2 = item[1], item[3]
    print(f"[{p1}, {p2}]")

conn.commit()

curs.execute(f'drop table {table}')
result = curs.fetchall()
print("全てのフィールド")
print(result)