"""Правила соляных пещер: удар героя, бой, покупка, цены и карточки врагов.

Случайный выбор врага остаётся в game.py, поэтому random здесь не нужен.
"""

prices = {"зелье": 10, "масло лампы": 15, "эликсир": 40}

enemy_stats = {
    "соляной голем": {"hp": 45, "damage": 6, "loot": 25},
    "кристальный паук": {"hp": 30, "damage": 4, "loot": 15},
    "солевая крыса": {"hp": 20, "damage": 3, "loot": 10},
    "светящийся червь": {"hp": 12, "damage": 2, "loot": 5},
}


def hero_hit(n, damage, crit_damage):
    """Урон героя в удар номер n.

    Каждый третий удар критический.
    Возвращает пару (hit, crit): урон и признак крита. Ничего не печатает.
    """
    if n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus, damage, crit_damage):
    """Бой с врагом до гибели одного из двоих.

    Карточка врага берётся из enemy_stats по имени: ключи hp, damage, loot.
    bonus прибавляется к урону героя после удвоения крита.
    Печатает строки раундов.
    Возвращает (rounds, won, hero_health, loot): таблицу раундов
    [номер, урон героя, урон врага], признак победы, здоровье после боя
    и трофеи (за поражение 0).
    """
    s = enemy_stats[enemy]
    hp = float(s["hp"])
    rounds = []
    n = 0
    print(f"Вы спускаетесь глубже. Навстречу выходит: {enemy}!")
    while hp > 0 and hero_health > 0:
        n += 1
        hit, crit = hero_hit(n, damage, crit_damage)
        hit += bonus
        hp -= hit
        line = f"Раунд {n}: вы наносите {hit:.1f}"
        if crit:
            line += " (крит!)"
        if hp <= 0:
            line += ". Враг падает."
            rounds.append([n, hit, 0])
        else:
            blow = s["damage"]
            hero_health -= blow
            line += f". Здоровье врага: {hp:.1f}. Враг бьёт на {blow}."
            rounds.append([n, hit, blow])
        print(line)
    won = hp <= 0
    loot = s["loot"] if won else 0
    return rounds, won, hero_health, loot


def buy(price, gold, quantity=1):
    """Покупает quantity штук товара по цене price за золото gold.

    quantity по умолчанию 1.
    Возвращает (gold_left, ok): остаток золота и признак успеха.
    Ничего не печатает.
    """
    c = price * quantity
    if gold >= c:
        return gold - c, True
    return gold, False


if __name__ == "__main__":
    r, w, h, l = fight("соляной голем", 100, 0, 20.5, 41.0)
    print(f"самотест: раундов {len(r)}, победа={w}, трофеи={l}")