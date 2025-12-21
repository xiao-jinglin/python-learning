"""
要求
while文を使う
リストを先頭から順番に処理する
連続して2回、偶数が出たら処理を終了する
それまでに処理した数値の 合計 を表示する
注意
終了条件となった 2つ目の偶数は合計に含めない
for文は禁止
"""
# 数値のリスト
numbers = [3, 6, 3, 5, 8, 2, 10, 1]

# 合計を保存する変数
total = 0

# インデックス用の変数
index = 0

# 直前の数が偶数かどうかを記録するフラグ
prev_even = False

# リストの範囲内で繰り返す
while index < len(numbers):
    n = numbers[index]

    # 現在の数が偶数かどうかを判定
    if n % 2 == 0:
        # 直前も偶数だった場合、終了条件を満たす
        if prev_even:
            break
        # 今回は偶数なので、フラグを True にする
        prev_even = True
    else:
        # 奇数が出たら、偶数連続はリセット
        prev_even = False

    # 合計に加える
    total += n

    # 次の要素へ
    index += 1

# 結果を表示
print("合計：", total)
