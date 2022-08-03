from pythonproject.service import Service


def print_hi():
    print(f"Hi, {Service().hello()}")


if __name__ == "__main__":
    print_hi()
