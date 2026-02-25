from datetime import datetime

def multi_line_input(label):
    lines = []
    while True:
        line = input(f"{label}: ")
        if line == "":
            break
        lines.append(line)
    return lines

now = datetime.now()
filename = now.strftime("Daily-%Y-%m-%d-%H-%M.md")

date_str = now.strftime("%Y-%m-%d")
weekday_map = {
    "Monday": "月", "Tuesday": "火", "Wednesday": "水",
    "Thursday": "木", "Friday": "金",
    "Saturday": "土", "Sunday": "日"
}
weekday_jp = weekday_map[now.strftime("%A")]

data = {
    "financial": [],
    "classes": [],
    "study": [],
    "game": [],
    "other": [],
    "reflection": {"good": [], "improve": [], "goal": []}
}

answered = {key: False for key in data.keys()}

while True:
    print("\n=== ジャンル選択 ===")
    print(f"1: Financial {'【回答済み】' if answered['financial'] else ''}")
    print(f"2: Classes-log {'【回答済み】' if answered['classes'] else ''}")
    print(f"3: Study-log {'【回答済み】' if answered['study'] else ''}")
    print(f"4: Game {'【回答済み】' if answered['game'] else ''}")
    print(f"5: Other {'【回答済み】' if answered['other'] else ''}")
    print(f"6: ふりかえり {'【回答済み】' if answered['reflection'] else ''}")
    print("0: 保存して終了")

    choice = input("番号を選択: ")

    # ===== Financial =====
    if choice == "1":
        total = 0
        items = []
        print("\n支出入力（空Enterで終了）")
        while True:
            item = input("モノ: ")
            if item == "":
                break
            price_input = input("値段: ")
            try:
                price = int(price_input)
            except:
                price = 0
            total += price
            items.append((item, price))
        data["financial"] = (items, total)
        answered["financial"] = True

    # ===== Classes =====
    elif choice == "2":
        classes = []
        for i in range(1, 8):
            print(f"\n{i}h（空Enterで終了）")
            subject = input("授業: ")
            if subject == "":
                break

        print("内容（空Enterで終了）")
        contents = []
        while True:
            cont = input("- ")
            if cont == "":
                break
            contents.append(cont)

        print("連絡（空Enterでスキップ）")
        notes = []
        while True:
            note = input("> ")
            if note == "":
                break
            notes.append(note)

        classes.append((subject, contents, notes))

        data["classes"] = classes
        answered["classes"] = True

    # ===== Study =====
    elif choice == "3":
        study = []
        print("\nStudy-log（空Enterで終了）")
        while True:
            subject = input("教科: ")
            if subject == "":
                break
            time = input("時間: ")
            content = input("内容: ")
            impression = input("感想: ")
            study.append((subject, time, content, impression))
        data["study"] = study
        answered["study"] = True

    # ===== Game =====
    elif choice == "4":
        game = []
        print("\nGame（空Enterで終了）")
        while True:
            name = input("ゲーム名: ")
            if name == "":
                break
            time = input("時間: ")
            content = input("内容: ")
            impression = input("感想: ")
            game.append((name, time, content, impression))
        data["game"] = game
        answered["game"] = True

    # ===== Other =====
    elif choice == "5":
        other = multi_line_input("Other")
        data["other"] = other
        answered["other"] = True

    # ===== Reflection =====
    elif choice == "6":
        print("\n今日良かったこと")
        good = multi_line_input("-")
        print("\n改善したいこと")
        improve = multi_line_input("-")
        print("\n明日の目標")
        goal = multi_line_input("-")
        data["reflection"] = {
            "good": good,
            "improve": improve,
            "goal": goal
        }
        answered["reflection"] = True

    elif choice == "0":
        break

# ===== Markdown生成 =====

content = f"# {date_str}（{weekday_jp}）\n\n---\n"

# Financial
content += "\n## 💰 Financial\n\n### 支出\n"
content += "| Products | Price |\n|----------|-------|\n"
if answered["financial"]:
    items, total = data["financial"]
    for item, price in items:
        content += f"| {item} | ¥{price} |\n"
    content += f"| **Total** | **¥{total}** |\n"
else:
    content += "|  |  |\n| **Total** | **¥** |\n"

# Classes
# Classes
content += "\n\n---\n\n## 🏫 Classes-log\n"

for subject, contents, notes in data["classes"]:
    content += f"\n### {subject}\n"

    for cont in contents:
        content += f"- {cont}\n"

    if notes:
        content += "\n>[!NOTE] 連絡\n"
        for note in notes:
            content += f"> {note}\n"

# Study
content += "\n\n---\n\n## 📚 Study-log\n"
for subject, time, cont, imp in data["study"]:
    content += f"- {subject} ({time})\n  - 内容: {cont}\n  - 感想: {imp}\n"

# Game
content += "\n\n---\n\n## 🎮 Game\n"
for name, time, cont, imp in data["game"]:
    content += f"- {name} ({time})\n  - 内容: {cont}\n  - 感想: {imp}\n"

# Other
content += "\n\n---\n\n## 🌙 Others\n"
for line in data["other"]:
    content += f"- {line}\n"

# Reflection
content += "\n\n---\n\n## 🔄 1日ふりかえり\n"

for g in data["reflection"]["good"]:
    content += f"- 良かったこと: {g}\n"

for i in data["reflection"]["improve"]:
    content += f"- 改善したいこと: {i}\n"

for g in data["reflection"]["goal"]:
    content += f"- 明日の目標: {g}\n"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n✅ {filename} を作成しました。")