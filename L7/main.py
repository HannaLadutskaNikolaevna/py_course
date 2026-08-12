import bank_logic

def run():
    menu = """
    --- БАНКОВСКАЯ СИСТЕМА ---
    1 - Show (показать счета)
    2 - Add (добавить счет)
    3 - Delete (удалить счет)
    4 - Change (изменить счет)
    exit - выйти
    """
    
    oper = input(menu + "\nВыберите операцию: ")
    
    while oper != "exit":
        if oper == "1":
            bank_logic.Show()
        elif oper == "2":
            bank_logic.Add()
        elif oper == "3":
            bank_logic.Delete()
        elif oper == "4":
            bank_logic.Change()
        else:
            print("Не понял операцию...")
        
        oper = input("\nВыберите операцию: ")


run()