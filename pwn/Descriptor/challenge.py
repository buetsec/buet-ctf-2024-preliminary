#!/usr/local/bin/python
import os


class Pyjail:
    def __init__(self):
        self.allowed_functions = {
            "os": os,
            "open": self.safe_open,
            "read": self.safe_read,
            "close": self.safe_close,
            "print": self.client_print,
        }
        self.flag_fd = None

    def safe_open(self, path, flags):
        if path == "flag.txt" and flags == os.O_RDONLY:
            self.flag_fd = os.open(path, flags)
            return self.flag_fd
        else:
            raise PermissionError("Access denied to the specified file.")

    def safe_read(self, fd, length):
        if fd == self.flag_fd:
            return os.read(fd, length).decode()
        else:
            raise PermissionError("Invalid file descriptor.")

    def safe_close(self, fd):
        if fd == self.flag_fd:
            os.close(fd)
            self.flag_fd = None
        else:
            raise PermissionError("Invalid file descriptor.")

    def client_print(self, *args):
        output = " ".join(str(arg) for arg in args) + "\n"
        print(output.encode())

    def execute(self, code):
        exec(code, {"__builtins__": self.allowed_functions})


def handle_client():
    print(b"Escape the Jail\n")

    pyjail = Pyjail()

    while True:
        print(b"Jail> ")
        user_input = input().strip()
        if user_input.lower() == "exit":
            break
        try:
            pyjail.execute(user_input)
        except Exception as e:
            print(f"Error: {e}\n".encode())


if __name__ == "__main__":
    handle_client()
