# 年齢を入力
age = int(input("年齢を入力してください："))

# 学生かどうかを入力（yes / no）
is_student = input("学生ですか？（yes / no）：")

# 会員かどうかを入力（yes / no）
is_member = input("会員ですか？（yes / no）：")

# 招待状を持っているかを入力（yes / no）
has_invitation = input("招待状を持っていますか？（yes / no）：")

# 条件判定
# 条件1：18歳以上
# 条件2：学生ではない（not を使用）
# 条件3：会員である、または招待状を持っている（or を使用）
if age >= 18 and not (is_student == "yes") and (is_member == "yes" or has_invitation == "yes"):
    print("入場できます")
else:
    print("入場できません")
