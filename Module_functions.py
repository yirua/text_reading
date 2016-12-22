


def check_line_length(line):
    if (len(line) !=7):
        return "The number of columns is not exactly 7."
    else:
        return "The number of Columns is exactly 7. "

def allUnique(x):
        seen = set()
        return not any(i in seen or seen.add(i) for i in x)
#check if the elements in the list are all integers
def check_integers(aList):
    check_int = True
    for s in aList:
        try:
            int(s)

        except ValueError:
            check_int = False

    return check_int