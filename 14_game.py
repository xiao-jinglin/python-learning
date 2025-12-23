import random

# 武器クラス
class Weapon:
    def __init__(self, name, min_damage, max_damage, crit_bonus=0, ignore_defense=False):
        self.name = name                    # 武器名
        self.min_damage = min_damage        # 最小ダメージ
        self.max_damage = max_damage        # 最大ダメージ
        self.crit_bonus = crit_bonus        # クリティカルボーナス
        self.ignore_defense = ignore_defense # 防御無視フラグ

# マント（防具）クラス
class Cloak:
    def __init__(self, name, defense, dodge_bonus, immunity, hp_bonus=0):
        self.name = name                    # マント名
        self.defense = defense              # 防御力
        self.dodge_bonus = dodge_bonus      # 回避ボーナス
        self.immunity = immunity            # ダメージ無効化確率
        self.hp_bonus = hp_bonus            # HPボーナス

# キャラクタークラス
class Character:
    def __init__(self, name, hp, power, defense, dodge, crit, skill):
        self.name = name                    # キャラクター名
        self.base_hp = hp                   # 基本HP
        self.hp = hp                        # 現在HP
        self.power = power                  # 攻撃力
        self.defense = defense              # 防御力
        self.dodge = dodge                  # 回避率
        self.crit = crit                    # クリティカル率
        self.skill = skill                  # 必殺技発動率
        self.weapon = None                  # 装備武器（初期なし）
        self.cloak = None                   # 装備マント（初期なし）

    # 武器を装備
    def equip_weapon(self, weapon):
        self.weapon = weapon

    # マントを装備
    def equip_cloak(self, cloak):
        self.cloak = cloak
        self.hp += cloak.hp_bonus           # 装備によるHPボーナス

    # 生存判定
    def is_alive(self):
        return self.hp > 0

    # 通常攻撃
    def attack(self, target):
        # 回避判定
        total_dodge = target.dodge + (target.cloak.dodge_bonus if target.cloak else 0)
        if random.random() < total_dodge:
            print(f"{target.name}は攻撃を回避した！")
            return

        # 無効化判定
        immunity = target.cloak.immunity if target.cloak else 0
        if random.random() < immunity:
            print(f"🛡️ {target.name} は攻撃を無効化した！")
            return

        # 武器ダメージ
        weapon_damage = 0
        if self.weapon:
            weapon_damage = random.randint(self.weapon.min_damage, self.weapon.max_damage)

        # 総ダメージ計算
        if self.weapon and self.weapon.ignore_defense:
            damage = self.power + weapon_damage
            print(f"🗡️ {self.weapon.name}：防御無視！")
        else:
            total_def = target.defense + (target.cloak.defense if target.cloak else 0)
            damage = self.power + weapon_damage - total_def

        # クリティカル判定
        crit_chance = self.crit + (self.weapon.crit_bonus if self.weapon else 0)
        if random.random() < crit_chance:
            damage *= 2
            print("💥 クリティカルヒット！")

        if damage < 0:
            damage = 0

        # ダメージ適用
        target.hp -= damage
        print(f"{self.name}の攻撃！{target.name}に{damage}のダメージ！")

    # 必殺技
    def special_attack(self, target):
        print(f"{self.name}は必殺技を繰り出した！")
        damage = 999
        target.hp -= damage
        print(f"{target.name}に{damage}のダメージ！")

    # ターン処理
    def take_turn(self, target):
        if random.random() < self.skill:
            self.special_attack(target)
        else:
            self.attack(target)


# 武器インスタンス
sword = Weapon("聖剣", 99, 199, crit_bonus=0.1, ignore_defense=True)
ice_sword = Weapon("氷の剣", 79, 159, crit_bonus=0.2, ignore_defense=False)

# マントインスタンス
hero_cloak = Cloak("勇者マント", 20, 0.2, 0.5, hp_bonus=20)
demon_cloak = Cloak("地のマント", 40, 0.1, 0.2, hp_bonus=0)

# キャラクターインスタンス
hero = Character("勇者", 100, 20, 20, 0.5, 0.3, 0.15)
demon = Character("魔王", 9999, 99, 99, 0.01, 0, 0)

# 装備
hero.equip_weapon(sword)
hero.equip_cloak(hero_cloak)
# 魔王は装備なし

# 戦闘関数
def battle(hero, demon):
    turn = 1
    print("=== 戦闘開始！===")
    while hero.is_alive() and demon.is_alive():
        print(f"\n--- 回合 {turn} ---")
        hero.take_turn(demon)
        if not demon.is_alive():
            print("🎉 勇者勝利！")
            break
        demon.take_turn(hero)
        if not hero.is_alive():
            print("💀 勇者敗北")
            break
        print(f"HP → 勇者:{hero.hp} / 魔王:{demon.hp}")
        turn += 1

battle(hero, demon)
