# ユーザー名を入力する
username = input("ユーザー名を入力してください：")

# ① まず長さをチェックする
# len() は文字列の長さを返す
if len(username) < 6 or len(username) > 12:
    # 長さが条件を満たしていない場合
    print("不正：長さが6〜12文字ではありません")

else:
    # ② 条件判定用のフラグ変数を用意する
    # アルファベットが含まれているか
    has_letter = False

    # すべて英数字かどうか
    is_alnum = True

    # ③ ユーザー名を1文字ずつ確認する
    for ch in username:

        # isalpha()：アルファベットかどうか
        if ch.isalpha():
            has_letter = True

        # isalnum()：英数字かどうか
        # 英数字でなければ False にする
        if not ch.isalnum():
            is_alnum = False

    # ④ ここから最終判定

    # 英数字以外が含まれている場合
    if not is_alnum:
        print("不正：英数字以外の文字が含まれています")

    # アルファベットが1文字も含まれていない場合
    elif not has_letter:
        print("不正：アルファベットが含まれていません")

    # すべての条件を満たしている場合
    else:
        print("有効なユーザー名です")
