# def Stringg(st: str):
#     if " " in st and "@" in st:
#         print("space + @ both found")
#     elif " " in st:
#         print("only space found")
#     elif "@" in st:
#         print("only @ found")
#     else:
#         print("none found")

# st = "hello ji kse ho @123"
# Stringg(st)


def Stringg(st: str):
    clean_text = ""
    space_found = False
    at_found = False

    for ch in st:
        if ch == " ":
            space_found = True
        if ch == "@":
            at_found = True

    if space_found:
        print("space found")
        clean_text = st.strip()   # correct
    else:
        print("no space")
        clean_text = st

    if at_found:
        print("@ found")

        clean_text=st.replace("@"," 😂😂")
    else:
        print("@ not found")

    print("Clean text:", clean_text)


st = "  hello ji kse ho 123 @@@@@ "
Stringg(st)