"""
次のタプルがあります：
scores = (88, 92, 76, 92, 85, 76)

要求：
このタプルの
要素数
最大値
最小値
を求めて出力してください
値 92 が 何回出現するか を求めて出力してください
タプルの 3番目の要素 を出力してください
（※ インデックスに注意）
このタプルを リストに変換 し、
最後に 100 を追加
その後、再びタプルに戻してください
"""

scores = (88, 92, 76, 92, 85, 76)   
# 要素数
print("要素数：", len(scores))
# 最大値
print("最大値：", max(scores))
# 最小値
print("最小値：", min(scores))
# 92の出現回数
print("92の出現回数：", scores.count(92))
# 3番目の要素（インデックス2）
print("3番目の要素：", scores[2])
# リストに変換して100を追加、その後タプルに戻す
score_list = list(scores)
score_list.append(100)
scores = tuple(score_list)
print("更新後のタプル：", scores)
