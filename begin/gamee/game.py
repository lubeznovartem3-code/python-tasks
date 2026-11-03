import json
import os
import random

import dungeon

try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False


class BadStats(ValueError):
    pass


title = "СОЛЯНЫЕ ПЕЩЕРЫ"
frame = "=" * (len(title) + 6)
base_attack = 10

MAP = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "#", ".", ".", "#"],
    ["#", ".", "#", "#", ".", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", ".", "#", ".", ".", "#"],
    ["#", "#", "S", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#"],
]
LOOT = {(1, 2): "соляной кристалл", (1, 5): "старая кирка", (4, 5): "блестящий самородок"}
DIRECTIONS = {"север": (-1, 0), "юг": (1, 0), "запад": (0, -1), "восток": (0, 1)}
EFFECTS = {
    "зелье": "+10 здоровья",
    "масло лампы": "+5 запаса сил",
    "эликсир": "+2 к урону до конца забега",
}

commands = [
    "осмотр", "идти [север|юг|запад|восток]", "отдых", "слушать", "лампа",
    "тренировка", "спуск", "рекорды", "магазин", "рюкзак", "пить [предмет]",
    "купить <предмет> [число]", "карта", "разведка", "заново", "помощь", "выход",
]
MENU = [
    "Что делаешь? (номер или команда; помощь — справка)",
    "1 - осмотреться (осмотр)",
    "2 - идти вперёд (идти)",
    "3 - отдохнуть (отдых)",
    "4 - прислушаться (слушать)",
    "5 - зажечь лампу (лампа)",
    "6 - тренировка (тренировка)",
    "7 - спуститься глубже (спуск)",
    "8 - таблица лидеров (рекорды)",
    "9 - магазин (магазин)",
    "10 - рюкзак (рюкзак)",
    "11 - выпить зелье (пить)",
    "0 - выйти из пещер (выход)",
    "без номеров: карта, разведка, заново",
]
num_to_verb = {
    "1": "осмотр", "2": "идти", "3": "отдых", "4": "слушать", "5": "лампа",
    "6": "тренировка", "7": "спуск", "8": "рекорды", "9": "магазин",
    "10": "рюкзак", "11": "пить", "0": "выход",
}


def paint(s, c):
    """Красит строку s цветом c ("green" или "yellow"), если есть colorama.

    Без colorama возвращает строку как есть.
    """
    if not COLOR:
        return s
    if c == "green":
        return Fore.GREEN + s + Style.RESET_ALL
    return Fore.YELLOW + s + Style.RESET_ALL


def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и рекорд врага. Возвращает None."""
    if not log:
        print("Вы ещё не сражались.")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
    worst = max(log, key=lambda r: r[2])
    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")


def print_run_summary(log):
    """Печатает суммарный и средний урон героя за забег. Возвращает None."""
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Раундов: {rounds}, общий урон: {total:.1f}, средний: {total / rounds:.1f}.")
    else:
        print("Боёв в этом забеге не было.")


def scout(r, c, seen):
    """Рекурсивно считает комнаты, доступные из клетки (r, c)."""
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total


def write_save():
    """Пишет состояние забега в save.json. Множества и кортежи — списками."""
    save = {}
    save["hero"] = hero_name
    save["health"] = health
    save["stamina"] = stamina
    save["gold"] = gold_total
    save["actions"] = actions
    save["damage"] = damage
    save["max_health"] = max_health
    save["max_stamina"] = max_stamina
    save["bonus"] = ability_bonus
    save["inventory"] = inventory
    save["log"] = log
    save["enemies"] = enemies
    save["position"] = [hero_r, hero_c]
    save["visited"] = sorted([list(p) for p in visited])
    save["loot"] = sorted(found_loot)
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False, indent=2)


print(frame)
print("   " + title + "   ")
print(frame)
print()

loaded = None
if os.path.exists("save.json"):
    print("Найдено сохранение. Продолжить забег? (да/нет)")
    answer = input().strip().lower()
    if answer in ("да", "yes"):
        try:
            with open("save.json", encoding="utf-8") as f:
                loaded = json.load(f)
        except (ValueError, OSError):
            print("Сохранение повреждено. Начинаем новый забег.")
    print()

enemies = list(dungeon.enemy_stats)
log = []
inventory = {}
gold_total = 0
ability_bonus = 0
actions = 0
hero_r, hero_c = 5, 2
visited = {(5, 2)}
found_loot = set()

if loaded is None:
    print("Как зовут героя?")
    hero_name = input()
    print(f"Добро пожаловать, {hero_name}!")
    print("Ты входишь в соляные пещеры. Здесь прохладно, а стены искрятся белыми кристаллами.")
    print()
    print("Настройка героя.")
    print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")
    while True:
        try:
            health = int(input())
            strength = int(input())
            agility = int(input())
            endurance = int(input())
            if health <= 0:
                raise BadStats(f"Здоровье должно быть положительным, а введено {health}")
            if strength < 0 or agility < 0 or endurance < 0:
                raise BadStats("Характеристики не могут быть отрицательными")
            if strength > 100:
                raise BadStats(f"Сила не может быть больше 100, а введено {strength}")
            break
        except BadStats as e:
            print(f"{e}. Введите все четыре снова:")
        except ValueError:
            print("Ой: одна из строк не число. Введите все четыре снова:")
    print()
    damage = base_attack + strength * 1.5
    crit_damage = damage * 2
    stamina = health // 10 + endurance
    max_health = health
    max_stamina = stamina
    print("Характеристики героя:")
    print(f"{'Здоровье:':<14}{health}")
    print(f"{'Сила:':<14}{strength}")
    print(f"{'Ловкость:':<14}{agility}")
    print(f"{'Выносливость:':<14}{endurance}")
    print()
    print(f"Урон героя: {damage:.1f}")
    print(f"Критический урон: {crit_damage:.1f}")
    print(f"Запас сил: {stamina}")
    print()
else:
    hero_name = loaded["hero"]
    health = loaded["health"]
    stamina = loaded["stamina"]
    gold_total = loaded["gold"]
    actions = loaded["actions"]
    damage = loaded["damage"]
    crit_damage = damage * 2
    max_health = loaded["max_health"]
    max_stamina = loaded["max_stamina"]
    ability_bonus = loaded["bonus"]
    inventory = loaded["inventory"]
    log = loaded["log"]
    enemies = loaded["enemies"]
    hero_r, hero_c = loaded["position"]
    visited = {tuple(p) for p in loaded["visited"]}
    found_loot = set(loaded["loot"])
    print(f"Забег продолжен: здоровье {health}, золото {gold_total}, врагов осталось {len(enemies)}.")
    print()

running = True
outcome = "прерывание"
try:
    while running:
        print("\n".join(MENU))
        print()
        line = input()
        cmd = line.strip().lower()
        while cmd == "":
            print("Пустая команда. Введи команду или номер.")
            line = input()
            cmd = line.strip().lower()
        words = cmd.split()
        verb = words[0]
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]
        match verb:
            case "осмотр":
                print("Вы осматриваетесь. Стены в белых разводах соли, с потолка свисают сталактиты.")

            case "идти":
                if len(words) > 1 and words[1] in DIRECTIONS:
                    dr, dc = DIRECTIONS[words[1]]
                    nr, nc = hero_r + dr, hero_c + dc
                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))
                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                print(f"Вы нашли: {item}! Уникальных находок: {len(found_loot)}.")
                        print(f"Вы делаете шаг: {words[1]}. Комната ({hero_r}, {hero_c}).")
                    else:
                        print(f"Нельзя идти на {words[1]}: стена или край карты.")
                else:
                    cost = 2
                    if stamina >= cost:
                        stamina -= cost
                        print("Вы осторожно идёте вперёд. Соль хрустит под ногами.")
                    else:
                        health -= cost - stamina
                        stamina = 0
                        print("Сил больше нет — вы идёте на одном упорстве.")

            case "отдых":
                stamina = min(stamina + 3, max_stamina)
                print("Вы садитесь на солёный выступ и переводите дух. Силы понемногу возвращаются.")

            case "слушать":
                print("Вы замираете. Где-то капает вода, а в глубине слышно, как скребутся враги.")
                print(f"Врагов в пещерах: {len(enemies)}.")

            case "лампа":
                if stamina >= 1:
                    stamina -= 1
                    print("Вы зажигаете лампу. Кристаллы на стенах вспыхивают розовым светом.")
                else:
                    print("Нет сил, чтобы зажечь лампу.")

            case "тренировка":
                strikes = 6
                cost = 3
                if stamina < cost:
                    print("Не хватает сил на тренировку.")
                else:
                    stamina -= cost
                    print("Вы подходите к глыбе соли, которую оставил здесь прошлый искатель.")
                    print()
                    print(f"Наносите ударов: {strikes}.")
                    total_damage = 0
                    crit_count = 0
                    for i in range(1, strikes + 1):
                        hit, crit = dungeon.hero_hit(i, damage, crit_damage)
                        total_damage += hit
                        if crit:
                            crit_count += 1
                            print(f"Удар {i}: {hit:.1f} — критический!")
                        else:
                            print(f"Удар {i}: {hit:.1f}")
                    print()
                    print(f"Итог: ударов {strikes}, критических: {crit_count}.")
                    print(f"Общий урон: {total_damage:.1f}")
                    print(f"Средний урон: {total_damage / strikes:.1f}")

            case "спуск":
                if not enemies:
                    print("Вы идёте глубже, но пещеры пусты: врагов больше нет.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = dungeon.fight(enemy, health, ability_bonus, damage, crit_damage)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(paint(f"Враг побеждён: {enemy}. Врагов осталось: {len(enemies)}. Трофеи: {loot} золота.", "yellow"))
                    print(f"Бой: раундов {len(rounds)}.")

            case "рекорды":
                print_leaderboard(log)

            case "магазин":
                print("Магазин:")
                for name, price in dungeon.prices.items():
                    print(f"{name}: {price} золота ({EFFECTS[name]})")
                print("Купить: купить <предмет> [число].")

            case "рюкзак":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Рюкзак:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")

            case "купить":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = " ".join(words[1:-1])
                else:
                    qty = 1
                    item = " ".join(words[1:])
                if item == "":
                    print("Что купить? Напиши: купить <предмет> [число].")
                    continue
                if item not in dungeon.prices:
                    print("Такого предмета в магазине нет.")
                    continue
                gold_total, ok = dungeon.buy(dungeon.prices[item], gold_total, quantity=qty)
                if ok:
                    inventory[item] = inventory.get(item, 0) + qty
                    print(f"Куплено: {item} x{qty} за {dungeon.prices[item] * qty} золота. Осталось золота: {gold_total}.")
                else:
                    print(f"Не хватает золота: нужно {dungeon.prices[item] * qty}, есть {gold_total}.")

            case "пить":
                item = " ".join(words[1:]) or "зелье"
                if inventory.get(item, 0) == 0:
                    print(f"В рюкзаке нет предмета: {item}.")
                else:
                    if item == "зелье":
                        health = min(health + 10, max_health)
                    elif item == "масло лампы":
                        stamina = min(stamina + 5, max_stamina)
                    elif item == "эликсир":
                        ability_bonus += 2
                    inventory[item] -= 1
                    if inventory[item] == 0:
                        del inventory[item]
                    print(f"Вы используете: {item}. Осталось: {inventory.get(item, 0)}.")

            case "карта":
                print("Карта:")
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        cell = "@" if (i, j) == (hero_r, hero_c) else MAP[i][j]
                        cells.append(cell)
                    print(" ".join(cells))

            case "разведка":
                seen = set()
                print(f"Разведка: доступных комнат — {scout(hero_r, hero_c, seen)}.")

            case "заново":
                if os.path.exists("save.json"):
                    os.remove("save.json")
                    print("Сохранение удалено. Следующий забег начнётся с нуля.")
                else:
                    print("Сохранения нет.")
                continue

            case "помощь":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0-11 работают как раньше.")

            case "выход":
                print("Вы поднимаетесь обратно к свету. Пещеры остаются позади.")
                write_save()
                print("Прогресс сохранён.")
                outcome = "выход"
                running = False

            case _:
                print(f"Не понимаю команду: '{line.strip()}'. Напиши 'помощь'.")
                continue

        if running:
            actions += 1
        if running or health <= 0:
            print()
            print(paint(f"Здоровье: {health} Запас сил: {stamina} Врагов осталось: {len(enemies)} Золото: {gold_total}", "green"))
        if health <= 0:
            print(f"{hero_name} падает без сил. Пещеры забирают ещё одного искателя.")
            if os.path.exists("save.json"):
                os.remove("save.json")
            outcome = "гибель"
            running = False
except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")
    write_save()
finally:
    if inventory:
        print("В рюкзаке осталось:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("В рюкзаке осталось: ничего.")
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print_run_summary(log)
    print(frame)