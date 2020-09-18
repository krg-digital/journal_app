from database import add_entry, get_entries


menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to the programming diary!"

def prompt_new_entry():
    entry_content = input("What have you learned today?\n")
    entry_date = input("Enter the date: ")

    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}:\n{entry['content']}\n\n")

print(welcome)

# Sample 'entries' list.
# entries = [
#     {"content": "Today I started learning programming.", "date": "01-01-2020"},
#     {"content": "I created my first SQLite database!", "date": "02-01-2020"},
#     {"content": "I finished writing my programming diary application.", "date": "03-01-2020"},
#     {"content": "Today I'm going to continue learning programming!", "date": "04-01-2020"},
# ]

# ':=' is the walrus operator.
# python >= 3.8 is require for its use. 
while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option, please try again!")
