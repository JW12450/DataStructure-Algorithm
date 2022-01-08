while True:
    try:
        sen = input()
        print(sen)
    except EOFError:
        break