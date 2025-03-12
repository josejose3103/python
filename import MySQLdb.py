import MySQLdb
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# フォントのパス（適宜修正）
font_path = "C:/Users/josej/AppData/Local/Microsoft/Windows/Fonts/ipaexg.ttf"
if not os.path.exists(font_path):
    font_path = "./fonts/ipaexg.ttf"  # フォントをプロジェクトフォルダに置く場合

# 日本語フォントの登録（IPAexゴシック）
pdfmetrics.registerFont(TTFont("IPAexGothic", font_path))

# データベース接続
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3103@Kazu",
    database="media"
)
cursor = conn.cursor()

# ユーザー入力の取得
start_date = input("開始日 (YYYY-MM-DD): ")
end_date = input("終了日 (YYYY-MM-DD): ")

# SQLクエリ
query = """
    SELECT noukamei, SUM(kingaku)
    FROM article3
    WHERE day BETWEEN %s AND %s
    GROUP BY noukamei
    ORDER BY kumikan;
"""
cursor.execute(query, (start_date, end_date))
results = cursor.fetchall()

# PDFファイルの作成
pdf_filename = "output.pdf"
c = canvas.Canvas(pdf_filename, pagesize=A4)
width, height = A4

# フォント設定（日本語対応）
c.setFont("IPAexGothic", 14)

# タイトル
c.drawString(50, height - 50, f"売上レポート ({start_date} 〜 {end_date})")

# ヘッダー
c.setFont("IPAexGothic", 12)
c.drawString(50, height - 80, "農家名")
c.drawString(300, height - 80, "合計金額")

# データを書き込む
y_position = height - 100
for row in results:
    noukamei, kingaku = row
    c.drawString(50, y_position, str(noukamei))
    c.drawString(300, y_position, str(kingaku))
    y_position -= 20  # 次の行へ

# PDFを保存
c.save()
conn.close()

print(f"PDFファイル '{pdf_filename}' を作成しました。")
