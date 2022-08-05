def quit_command_1(argv):
    import re

    pattern = re.search(r'^(\d+)q$', argv[1])
    if pattern:
        num = int(pattern.group(1))
        start = 1
        for line in sys.stdin:
            print(line, end="")
            if start == num:
                break
            start += 1
        return

    pattern = re.search(r'^/(.*)/q$', sys.argv[1])
    if pattern:
        regex = pattern.group(1)
        for line in sys.stdin:
            print(line, end="")
            if re.search(regex, line):
                break