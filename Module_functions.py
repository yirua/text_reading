


def check_line_length(lines):
    check_col_is_7 = True
    line_index = 1
    for line in lines:
        if (len(line) != 7):
            check_col_is_7 = False
            print "The line with not 7 columns: "
            print "line_index  {} : {}".format(line_index, line)

        #else:
        #    print "The line with 7 columns: "
        #    print line
        line_index += 1
    return check_col_is_7

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

#get the number of certain string in a list
def check_num_string(list, input):
    num_of_string =0
    for line in list:
        for s_str in line:
            if (s_str == input):
                num_of_string +=1

    return num_of_string