def main():
    lines = []
    print("Enter lines of text (press Ctrl-D to finish):")

    try:
        while True:
            line = input()
            lines.append(line)

    except EOFError:
        # pass

        print("\nReversed lines:")

        for line in reversed(lines):
            print(line)

if __name__ == "__main__":
    main()