from functions.run_python_file import run_python_file


def main():
    print("Result for running 'main.py' with no args:")
    result1 = run_python_file("calculator", "main.py")
    print(result1)
    print()

    print("Result for running 'main.py' with '3 + 5':")
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result2)
    print()

    print("Result for running 'tests.py':")
    result3 = run_python_file("calculator", "tests.py")
    print(result3)
    print()

    print("Result for running '../main.py':")
    result4 = run_python_file("calculator", "../main.py")
    print(result4)
    print()

    print("Result for running 'nonexistent.py':")
    result5 = run_python_file("calculator", "nonexistent.py")
    print(result5)
    print()

    print("Result for running 'lorem.txt':")
    result6 = run_python_file("calculator", "lorem.txt")
    print(result6)


if __name__ == "__main__":
    main()
