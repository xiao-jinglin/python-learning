"""
問題：有効な点数のみで平均と判定を行う関数
次の点数リストがあります。
scores = [80, -5, 70, 200, 70, 60]
要求
関数（def） を使うこと
点数リストを 引数 として受け取ること
0〜100（含む） の点数のみを有効とする
有効な点数の 平均点 を計算する
有効な点数が1つもない場合は
"データなし" を return する
有効な点数がある場合は
平均が 70以上 → "合格"
平均が 70未満 → "不合格"
関数を呼び出して、結果を表示すること
"""

def evaluate_scores(scores):
    # 有効な点数を保存するリスト
    valid_scores = []

    # 点数リストを順番に処理
    for score in scores:
        # 点数が0〜100の範囲内かどうかを判定
        if 0 <= score <= 100:
            valid_scores.append(score)

    # 有効な点数が1つもない場合
    if len(valid_scores) == 0:
        return "データなし"

    # 有効な点数の平均を計算
    average = sum(valid_scores) / len(valid_scores)

    # 平均点に基づいて判定を返す
    if average >= 70:
        return "合格"
    else:
        return "不合格"
    
scores = [80, -5, 70, 200, 90, 60]
result = evaluate_scores(scores)
print("判定結果：", result)
