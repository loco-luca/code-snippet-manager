# manager
import os
import json


def get_file_path(lang):
    os.makedirs("snippets", exist_ok=True)
    return f"snippets/{lang.lower()}.json"


def add(lang, snippets):
    file_path = get_file_path(lang)
    os.makedirs("snippets", exist_ok=True)

    # If file exists, load existing snippets
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    # Append the new snippets
    data.append(snippets)

    # Write updated data back to file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def delete(item, lang):
    path = get_file_path(lang)
    with open(path, "r") as f:
        data = json.load(f)
    new_data = [snippet for snippet in data if snippet["title"] != item]
    with open(path, "w") as f:
        json.dump(new_data, f, indent=4)

    print(f"Deleted snippet(s) with title '{item}' (if existed).")


def search(words, lang):
    path = get_file_path(lang)
    with open(path, "r") as f:
        data = json.load(f)

    for word in data:
        if word["title"] in words:
            print(word)


def view_snippets(lang):
    path = get_file_path(lang)
    with open(
        path,
        "r",
    ) as json_file:
        data = json.load(json_file)
        print(data)


def view_options():
    # user Options viewer
    print("Options avaliable are: ")
    print("1. Add a snippet")
    print("2. Delete a snippet")
    print("3. Search snippets")
    print("4. View all snippets")
