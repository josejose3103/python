import pyodbc
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime

# データベース接続
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\josej\OneDrive\Documents\カルテ.mdb;'
)
conn = pyodbc.connect(conn_str)

# SQLクエリ実行
sql = "SELECT フィールド４, sum(フィールド3) FROM 保険外　薬品 WHERE フィールド1 BETWEEN #2025/02/01# AND #2025/03/31# GROUP BY フィールド４"
df = pd.read_sql(sql, conn)

# 列名を設定
df.columns = ['Name', 'Amount']  # 英語に変更

# PDFファイル名を設定
current_date = datetime.now().strftime("%Y%m%d")
pdf_filename = f"Insurance_Bill_{current_date}.pdf"

# ReportLabでPDF作成
doc = SimpleDocTemplate(pdf_filename, pagesize=A4)
elements = []

# タイトル行をデータに含める
data = [['Insurance Bill - Non-covered Items', ''], 
        ['Period: 2025/02/01 - 2025/03/31', ''],
        ['', ''],  # 空白行
        ['Name', 'Amount']]  # ヘッダー行

# データ行を追加
total = 0
for i, row in df.iterrows():
    data.append([str(row["Name"]), str(row["Amount"])])
    total += row["Amount"]

# 合計行を追加
data.append(['Total', str(total)])

# テーブル作成
table = Table(data, colWidths=[300, 240])
table.setStyle(TableStyle([
    # タイトル行のスタイル
    ('SPAN', (0, 0), (1, 0)),  # タイトル行を結合
    ('SPAN', (0, 1), (1, 1)),  # 期間行を結合
    ('ALIGN', (0, 0), (0, 1), 'CENTER'),  # タイトルと期間を中央揃え
    ('FONTSIZE', (0, 0), (0, 0), 16),  # タイトルのフォントサイズ
    
    # ヘッダー行のスタイル
    ('BACKGROUND', (0, 3), (1, 3), colors.grey),
    ('TEXTCOLOR', (0, 3), (1, 3), colors.whitesmoke),
    
    # すべてのセルの基本スタイル
    ('ALIGN', (0, 3), (1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (1, -1), 'Helvetica'),
    
    # 合計行のスタイル
    ('BACKGROUND', (0, -1), (1, -1), colors.lightgrey),
    
    # セルの罫線
    ('GRID', (0, 3), (1, -1), 1, colors.black),
    ('BOX', (0, 3), (1, -1), 1, colors.black),
]))

elements.append(table)

# PDF生成
doc.build(elements)
print(f"PDFファイルが正常に作成されました: {pdf_filename}")

# 接続を閉じる
conn.close()