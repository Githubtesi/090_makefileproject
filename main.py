# ----------------------------
# 090 ファイルの作成

# ファイル操作...いろんな種類がある
# https://docs.python.org/ja/3/library/filesys.html

# ファイルの書き込み
# 注意、ファイルが空ファイルで上書きされる。

# 組み込み関数のopen
# https://docs.python.org/ja/3/library/functions.html#open

# openしたらcloseする
# ファイルオープン→読み書き→クローズ
# ----------------------------

# 参考:ファイルの指定をGUIで実施
# __file_daialog

#1.ファイルの指定
# ファイル名
fileName = r"test.txt"

#2.ファイルのオープン
# ファイルのオープン
f = open(fileName, "w")

#3 書き込み
# 書き込み方法1
f.write("test\n")

# 書き込み方法2
# print("My", "name", "is", "yoshiaki", sep=" ", file=f)

# 4 ファイルを閉じる
# ファイルを閉じる
f.close()
