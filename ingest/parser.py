import os


def load_files(folder, exts):

    docs = []

    for root, _, files in os.walk(folder):
        for f in files:
            if f.endswith(exts):
                path = os.path.join(root, f)

                with open(path, "r", encoding="utf-8", errors="ignore") as file:
                    text = file.read()

                docs.append({
                    "path": path,
                    "text": text
                })

    return docs


def load_all():

    notes = load_files("data/notes", (".md",))
    code = load_files("data/code", (".py", ".js", ".ts", ".cpp"))

    return notes + code
