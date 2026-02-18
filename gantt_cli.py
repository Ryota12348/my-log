def create_task(section_name):
    name = input("課題名: ")
    start = input("開始日(MM-DD): ")
    duration = input("作業日数: ")
    target = input("目標完了日(MM-DD): ")
    deadline = input("提出期限(MM-DD): ")

    checklist = f"- [ ] {name}（{deadline}提出）\n"

    gantt = f"""    {name} 作業     :active, {start}, {duration}d
    {name} 目標完了 :milestone, {target}, 0d
    {name} 提出期限 :crit, milestone, {deadline}, 0d
"""

    return checklist, gantt


def main():
    title = input("タイトル: ")

    checklist_content = ""
    gantt_content = ""

    while True:
        section_name = input("\nセクション名（例: 数学）: ")
        gantt_content += f"\n    section {section_name}\n"

        while True:
            add_task = input("課題を追加しますか？(y/n): ")
            if add_task.lower() != "y":
                break

            checklist, gantt = create_task(section_name)
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
    excludes weekends
{gantt_content}
```
"""

    with open("task_progress.md", "w", encoding="utf-8") as f:
        f.write(markdown)

    print("\n✅ task_progress.md を生成しました！")


if __name__ == "__main__":
    main()
