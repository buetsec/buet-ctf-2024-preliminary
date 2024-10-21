def secret(key):
    val = 0x4F
    p1 = "{7ctLj4"
    p2 = "FSqgAcpFMrU3qhfu1jNpf"[::-1]
    p3 = ""
    x = 16
    for c in rb"\)\umQDqpk`h(jL":
        p3 += chr(c ^ x)
        x += 1
    key = key[1]
    p4 = chr((ord(key) // ord(key)) * 87)
    p5 = ""
    for c in "ALs[":
        enc = ord(c)
        sub = (enc - 69) % 128
        p5 += chr(sub ^ val)
    p6 = "L}"
    flag = p1 + p2 + p3 + p4 + p5 + p6
    return "{8hHVpauQQYxfSCQodUoBn8uZWY9Pi952QC9WP13oDpQNt9cswHJxdBbadrY}"


def grid():
    user_input = input(">> ")

    restricted_keywords = [
        "import",
        "os",
        "sys",
        "eval",
        "exec",
        "__builtins__",
        "__globals__",
        "__getattribute__",
        "__dict__",
        "__base__",
        "__class__",
        "__subclasses__",
        "dir",
        "help",
        "exit",
        "open",
        "read",
        "grid()",
        "main()",
        "replace",
        "=",
    ]

    is_input_valid = True
    for keyword in restricted_keywords:
        if keyword in user_input:
            print("Attempting something unusual, aren't you?")
            is_input_valid = False
            break
    for char in user_input:
        if ord(char) < 23 or ord(char) > 126:
            print("Attempting something unusual, aren't you?")
            is_input_valid = False
            break

    if is_input_valid:
        try:
            exec(
                user_input,
                {"__builtins__": {"print": print}},
                {"secret": secret, "main": main, "grid": grid},
            )
        except:
            print("Hey, an error occured! But which one...")


def main():
    try:
        while True:
            grid()
    except KeyboardInterrupt:
        print("GoodBye!!")


if __name__ == "__main__":
    main()
