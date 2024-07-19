tasks = {}
task_id = 1

while True:
    print("")
    print("- - - - - - - - - -")
    print("1：タスクを追加🆕")
    print("2：タスクを表示👀")
    print("3：タスクを削除🗑️")
    print("4：タスクを検索🔍")
    print("5：作業を終了🛑")
    print("- - - - - - - - - -")
    print("")

    user = input("選択肢を入力してください：")

    if user == "1":
        task_name = input("追加するタスク名を入力してください：")
        tasks[task_id] = task_name
        print("【タスクが追加されました🆕】")
        task_id = task_id + 1

    elif user == "2":
        if len(tasks) == 0:
            print("【タスクはありません❌】")
        else:
            print("【表示結果👀】")
            for id in tasks:
                name = tasks[id]
                print(f"{id}: {name}")

    elif user == "3":
        del_id = int(input("削除するタスクIDを入力してください:"))
        if del_id in tasks:
            del tasks[del_id]
            print("【タスクが削除されました🗑️】")
        else:
            print("【タスクはありません❌】")

    elif user == "4":
        search_name = input("検索するタスク名を入力してください：")
        search_tasks = []
        for id in tasks:
            name = tasks[id]
            if search_name in name:
                search_tasks.append(f"{id}: {name}")
        if search_tasks:
            print("【検索結果🔍】")
            for result in search_tasks:
                print(result)
        else:
            print("【タスクはありません❌】")

    elif user == "5":
        print("作業を終了します🛑")
        break

    else:
        print("無効な選択肢です🚨もう一度試してください👀")
