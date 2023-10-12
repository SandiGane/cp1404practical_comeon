"""
Create menu based on pseudocode in Prac1 outline
"""

MENU = ["(H)ello\n(G)oodbye\n(Q)uit"]
name = input("Enter name: ")
for i in MENU:
    print(i)
    choice = input(">>> ")
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
        for i in MENU:
            print(i, sep=" ")
            choice = input(">>> ")
    elif choice == "G":
        print(f"Goodbye {name}")
        for i in MENU:
            print(i, sep=" ")
            choice = input(">>> ")
    else:
        print("Invalid choice")
        for i in MENU:
            print(i)
            choice = input(">>> ")
print("Finished.")
