def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__': # ei jaigay if__name__ == '__main__'" eita dilew hobe na dilew hobe..
    line = input()
    result = split_and_join(line)
    print(result)
