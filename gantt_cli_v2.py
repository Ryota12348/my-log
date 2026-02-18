import os

def create_task():
    name = input("課題名: ")
    start = input("開始日(MM-DD): ")
    duration = input("作業日数: ")
    deadline = input("提出期限(MM-DD): ")

    checklist = f"- [ ] {name}（{deadline}提出）\n"

    gantt = f"""    {name}     :active, {start}, {duration}d
    {name} 提出期限 :crit, milestone, {deadline}, 0d
"""

    return checklist, gantt


def generate_content(title):
    checklist_content = ""
    gantt_content = ""

    while True:
        section_name = input("\nセクション名（例: 数学）: ")
        gantt_content += f"\n    section {section_name}\n"

        while True:
            add_task = input("課題を追加しますか？(y/n): ")
            if add_task.lower() != "y":
                break

            checklist, gantt = create_task()
            checklist_content += checklist
            gantt_content += gantt

        add_section = input("別のセクションを追加しますか？(y/n): ")
        if add_section.lower() != "y":
            break

    markdown = f"""# Task Progress

## tasks
{checklist_content}

## Gantt

```mermaid
gantt
    title {title}
    dateFormat  MM-DD
    axisFormat %m/%d
    tickInterval 2day
{gantt_content}
```
"""

    return markdown


def main():
    print("1: 新規作成")
    print("2: 既存ファイルに追記")
    mode = input("番号を選んでください: ")

    filename = input("ファイル名（例: task_progress.md）: ")
    title = input("タイトル: ")

    content = generate_content(title)

    if mode == "1":
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n✅ {filename} を新規作成しました！")

    elif mode == "2":
        if not os.path.exists(filename):
            print("⚠ ファイルが存在しません。新規作成します。")
        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n\n" + content)
        print(f"\n✅ {filename} に追記しました！")

    else:
        print("無効な入力です。")


if __name__ == "__main__":
    main()
