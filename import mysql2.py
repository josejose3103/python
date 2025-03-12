import mysql.connector

# ユーザー入力（例）
start_day = input("開始日を入力（YYYY-MM-DD）: ")
end_day = input("終了日を入力（YYYY-MM-DD）: ")
kumikanbangou = input("組勘番号を入力: ")

# MySQLデータベース接続
conn = mysql.connector.connect(
    host="localhost",      # MySQLサーバーのホスト名（例: localhost）
    user="root",  # MySQLのユーザー名
    password="3103@Kazu",  # MySQLのパスワード
    database="media"  # 使用するデータベース名
)
cursor = conn.cursor()

# SQL実行（%s を使用）
query = """
SELECT number, byoumei, kingaku 
FROM article3 
WHERE day BETWEEN %s AND %s 
AND kumikanbangou = %s;
"""
cursor.execute(query, (start_day, end_day, kumikanbangou))

# 結果を取得
rows = cursor.fetchall()
for row in rows:
    print(row)

# 接続を閉じる
cursor.close()
conn.close()
