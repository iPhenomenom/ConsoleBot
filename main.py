phone_book = {}

def hello():

    a = input(str()).lower()
    if a == "hello":
        print('How can I help you?')
        main()
    elif a == "." or a == "exit" or a == "good bye" or a == "close":
        raise SystemExit('Good bye')

    elif a != "hello":
        print('Print "Hello" for Start')
        hello()


def main():
    data = input(str()).lower()

    if data == "." or data == "exit" or data == "good bye" or data == "close":
        raise SystemExit('Good bye')

    elif 'add' in data:
        add_phone(data)

    elif "change" in data:
        change(data)

    elif "phone" in data:
        phone(data)

    elif "show all" in data:
        show_all()

    elif "" in data:
        print('try again')
        main()
    elif " " in data:
        print('try again')
        main()


def add_phone(data):
    a = data.split()
    a.remove("add")
    try:
        f = dict([a])
    except ValueError:
        print(f"Give me name and phone please")
        main()
    else:
        phone_book.update(f)
        print("Phone add on Phone book")
        main()

def change(data):
    a = data.split()
    a.remove("change")
    try:
        f = dict([a])
    except ValueError:
        print(f"Give me name and phone please")
        main()
    else:
        phone_book.update(f)
        print("Number is change")
        main()

def phone(data):
    a = data.split()
    a.remove("phone")
    a = a[0]
    try:
        print(f"{a} : {phone_book[a]}")
    except KeyError:
        print(f"Name {a} is not in Phone Book")
        main()
    else:
        main()

def show_all():
    for key, value in phone_book.items():
        print("{0} : {1}".format(key, value))
    main()


if __name__ == '__main__':
    print('Print "Hello" for Start')
    hello()


