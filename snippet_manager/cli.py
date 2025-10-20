# cli
from .manager import (
    delete,
    add,
    search,
    view_options,
    view_snippets,
)
from .utils import data_generator_formatted
from .logo import ascii_logo


def system():
    ascii_logo()
    print("\n")
    languages = ["Python", "Rust", "Dart"]

    while True:
        print(f"Currently languages supported -> {languages}")
        user_input = input("Select a language or 'q' to quit: ").strip()

        # dealing with empty inputs
        if not user_input.strip():
            print("Please enter your choice")
            continue

        # closing program logic
        if user_input.lower() == "q":
            confirm = input("Are you sure want to quit out of program? (y/n): ")
            if confirm.lower() == "y":
                print("Closing Code snippet manager ")
                break
            elif confirm.lower() == "n":
                print("sound bro👌")
                continue
            else:
                print("You good bro? 🤨")

        # if statement for manager logic
        confirm_choice = input(f"Are you sure you want {user_input}? (y/n): ").strip()

        if confirm_choice.lower() == "y":
            # displays option
            view_options()
            try:
                user_options_choices = int(
                    input("Enter a number that match your choices: ")
                )
            except ValueError:
                print("Invalid number. Please try again.")
                continue

            if user_options_choices == 1:
                code_snippet = data_generator_formatted(user_input)
                add(code_snippet)

            elif user_options_choices == 2:
                delete_term = input("Please enter title: ").strip()
                delete(delete_term, user_input)

            elif user_options_choices == 3:
                search_term = input("search: ").strip()
                search(search_term, user_input)

            elif user_options_choices == 4:
                view_snippets(user_input)
                print("view_snippets")
            else:
                print("No further option from this point onwards")
