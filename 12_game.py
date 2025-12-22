import random

def normal_attack(attacker, defender):

    weapon = weapon_list.get(attacker["weapon_name"], {})
    cloak = cloaks_list.get(defender["cloak_name"], {})

    # 回避判定
    total_dodge = defender["dodge"] + cloak.get("dodge_bonus", 0)
    if random.random() < total_dodge:
        print(defender["name"] + "は攻撃を回避した！")
        return
    
    immunity = cloak.get("immunity", 0)
    if random.random() < immunity:
        print(f"🛡️ {defender['name']} は攻撃を無効化した！")
        return
    
    # ダメージ計算
    min_d =weapon.get("min_damage", 0)
    max_d =weapon.get("max_damage", 0)
    weapon_damage = random.randint(min_d, max_d) if min_d and max_d else 0

    if weapon.get("ignore_defense", False):
        damage = attacker["power"] + weapon_damage
        print(f"🗡️ {attacker['weapon_name']}：无视防御！")
    else:  
        total_def = defender["defense"] + cloak.get("defense", 0)
        damage = attacker["power"] + weapon_damage - total_def

    # クリティカル判定
    crit_chance = attacker["crit"] + weapon.get("crit_bonus", 0)
    if random.random() < crit_chance:
        damage *= 2
        print("💥 クリティカルヒット！")

    if damage < 0:
        damage = 0

    defender["hp"] -= damage
    print(f"{attacker['name']}の攻撃！{defender['name']}に{damage}のダメージ！")

def special_attack(attacker, defender):
    print(f"{attacker['name']}は必殺技を繰り出した！")
    damage = 9999
    defender["hp"] -= damage
    print(f"{defender['name']}に{damage}のダメージ！")

def take_turn(attacker, defender):
    if random.random() < attacker.get("skill", 0):
        special_attack(attacker, defender)
    else:
        normal_attack(attacker, defender)

          
hero = {
    "name": "勇者",
    "hp": 100,
    "power": 20,
    "defense": 20,
    "dodge": 0.5,
    "crit": 0.3,
    "skill": 0.05,

    "weapon_name": "聖剣",
    "cloak_name": "勇者マント"
}

demon = {
    "name": "魔王",
    "hp": 9999,
    "power": 99,
    "defense": 99,
    "crit": 0.01,
    "dodge": 0,

    "weapon_name": None,
    "cloak_name": None
}

weapon_list = {
    "聖剣":{ "min_damage": 99,
             "max_damage": 199, 
             "crit_bonus": 0.1, 
             "ignore_defense": True
             },
    "氷の剣":{"min_damage": 79, 
             "max_damage": 159, 
             "crit_bonus": 0.2, 
             "ignore_defense": False
             }
}

cloaks_list = {
    "勇者マント":{"defense": 20,
                "dodge_bonus": 0.2,
                "immunity": 0.5,
                "hp_bonus": 20
                },
    "地のマント":{"defense": 40,
                "dodge_bonus": 0.1,
                "immunity": 0.2,
                }     
}

hero_cloak = cloaks_list.get(hero["cloak_name"], {})
hero["hp"] += hero_cloak.get("hp_bonus", 0)

def battle(hero, demon):
    turn = 1
    print("=== 戦闘開始！===")
    while hero["hp"] > 0 and demon["hp"] > 0:
        print(f"\n--- ターン {turn} ---")

        # 勇者ラウンド
        take_turn(hero, demon)
        if demon["hp"] <= 0:
            print("🎉 勇者勝利！")
            return "win"
        
        # 魔王ラウンド
        take_turn(demon, hero)
        if hero["hp"] <= 0:
            print("💀 勇者敗北")
            return "lose"

        print(f"HP → 勇者:{hero['hp']} / 魔王:{demon['hp']}")
        turn += 1

battle(hero, demon)
