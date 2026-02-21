from datetime import date

filename = "英語の重要表現まとめ.md"

def initialize_file():
    try:
        with open(filename, "x", encoding="utf-8") as f:
            f.write(f"# 英語の重要表現まとめ\n\n作成日: {date.today()}\n\n---\n\n")
    except FileExistsError:
        pass  # すでに存在する場合は何もしない

def add_expression():
    expression = input("表現: ")
    meaning = input("意味: ")
    example = input("例文: ")

    entry = f"""## {expression}

- 意味: {meaning}
- 例文: {example}

---
"""

    confirm = input("追加しますか？(y/n): ")

    if confirm.lower() == "y":
        with open(filename, "a", encoding="utf-8") as f:
            f.write(entry)
        print("追加しました！\n")
    else:
        print("キャンセルしました。\n")

def main():
    initialize_file()
    print("英語重要表現 CLI モード\n")

    while True:
        add_expression()
        cont = input("続けますか？(y/n): ")
        if cont.lower() != "y":
            break

    print("終了しました。")

if __name__ == "__main__":
    main()