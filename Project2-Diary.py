# Digital Dagbok
import datetime
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M")


def read_diary():
    try:
        with open("diaryfile.txt", "r") as f:
            content = f.read()
            print("\n Your entries to the Diary \n")
            print(content)
            print("\n End of entries. \n")
    except FileNotFoundError:
        print("Sorry bro, your diary is lost in the universe.")


def write_diary(entry):
    try:
        with open("diaryfile.txt", "a") as f:
            f.write(f"{timestamp} {entry} \n")
            print("Thank you for your diary entry, bro.")
    except FileNotFoundError:
        print("Sorry, your entry was declined.")


while True:
    print("What would you like to do today?")
    print("1. Read your diary")
    print("2. Write in your diary")
    print("3. Quit")

    choice = input("Pick 1, 2 or 3.")

    if choice == "1":
        print(read_diary())
    elif choice == "2":
        entry = input("\n What would you like to write in your diary? \n")
        write_diary(entry)
    elif choice == "3":
        print("Don't forget to write something tomorrow.")
        break
    else:
        print("Invalid choice. Try again")
        break
