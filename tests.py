from functions.get_file_content import get_file_content


def main():
    # Test 1: Read main.py
    print("Result for 'main.py':")
    result1 = get_file_content("calculator", "main.py")
    print(result1)
    print()

    # Test 2: Read pkg/calculator.py
    print("Result for 'pkg/calculator.py':")
    result2 = get_file_content("calculator", "pkg/calculator.py")
    print(result2)
    print()

    # Test 3: Try to read outside working directory
    print("Result for '/bin/cat':")
    result3 = get_file_content("calculator", "/bin/cat")
    print(result3)
    print()

    # Test 4: Try to read non-existent file
    print("Result for 'pkg/does_not_exist.py':")
    result4 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result4)


if __name__ == "__main__":
    main()
