from datetime import datetime

def multi_input(title):
    print(f"\n{title}（空Enterで終了）")
    lines = []
    while True:
        line = input("- ")
        if line == "":
            break
        lines.append(line)
    return lines

# ===== 初期設定 =====
now = datetime.now()
filename = now.strftime("Daily-%Y-%m-%d-%H-%M.md")

date_str = now.strftime("%Y-%m-%d")
weekday_str = now.strftime("%A")

weekday_map = {
    "Monday": "月", "Tuesday": "火", "Wednesday": "水",
    "Thursday": "木", "Friday": "金",
    "Saturday": "土", "Sunday": "日"
}
weekday_jp = weekday_map.get(weekday_str, "")

# 各セクション保存用
data = {
    "financial": [],
    "classes": [],
    "study": [],
    "game": [],
    "others": [],
    "reflection": []
}

print("📘 日報CLI（好きなジャンルから入力）")

# ===== メニュー式入力 =====
while True:
    print("""
1: Financial
2: Classes-log
3: Study-log
4: Game
5: Others
6: ふりかえり
0: 保存して終了
""")

    choice = input("番号を選択: ")

    if choice == "1":
        data["financial"] = multi_input("💰 Financial")
    elif choice == "2":
        data["classes"] = multi_input("🏫 Classes-log")
    elif choice == "3":
        data["study"] = multi_input("📚 Study-log")
    elif choice == "4":
        data["game"] = multi_input("🎮 Game")
    elif choice == "5":
        data["others"] = multi_input("🌙 Others")
    elif choice == "6":
        data["reflection"] = multi_input("🔄 1日ふりかえり")
    elif choice == "0":
        break
    else:
        print("無効な入力")

# ===== Markdown生成 =====

content = f"# {date_str}（{weekday_jp}）\n\n---\n"

content += "\n## 💰 Financial\n"
for line in data["financial"]:
    content += f"- {line}\n"

content += "\n---\n\n## 🏫 Classes-log\n"
for line in data["classes"]:
    content += f"- {line}\n"

content += "\n---\n\n## 📚 Study-log\n"
for line in data["study"]:
    content += f"- {line}\n"

content += "\n---\n\n## 🎮 Game\n"
for line in data["game"]:
    content += f"- {line}\n"

content += "\n---\n\n## 🌙 Others\n"
for line in data["others"]:
    content += f"- {line}\n"

content += "\n---\n\n## 🔄 1日ふりかえり\n"
for line in data["reflection"]:
    content += f"- {line}\n"

# 保存
with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n✅ {filename} を作成しました。")