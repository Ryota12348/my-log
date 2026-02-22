from datetime import datetime

# 現在日時
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d-%H-%M")

# ===== 初期入力 =====
base_filename = input("ファイル名（必須）: ").strip()
title = input("タイトル（H1）: ").strip()

if base_filename == "":
    base_filename = "English-phrases"

# 日時を付与
filename = f"{base_filename}-{timestamp}.md"

if title == "":
    title = base_filename

# ===== ファイル作成 =====
with open(filename, "w", encoding="utf-8") as f:
    f.write(
        f"# {title}\n\n"
        f"作成日時: {now.strftime('%Y-%m-%d %H:%M')}\n\n"
        f"---\n\n"
    )

print(f"\n{filename} を作成しました。")
print("英語重要表現 CLI（終了: Ctrl+C）\n")

# ===== 入力ループ =====
try:
    while True:
        expression = input("表現: ")
        meaning = input("意味: ")

        entry = f"""## {expression}

- 意味: {meaning}

---

"""

        with open(filename, "a", encoding="utf-8") as f:
            f.write(entry)

        print("追加しました。\n")

except KeyboardInterrupt:
    print("\n終了しました。")