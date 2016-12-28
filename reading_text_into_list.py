import csv
import Module_functions
Col1= []

Col5= []

line_list = []
with open('ColCheckMe','r') as f:
   # next(f) # skip headings
    fields = []
    for line in f:
        fields = line.split('\t')
        line_list.append(fields)
#    print 'the length of fields: \n'
#    print len(fields)
#    print '\n'

line_len_check = Module_functions.check_line_length(line_list)
print "The columns in the file are 7 in each line: "
print line_len_check

print "The number of SpecStr in the file: "
check_str = "SpecStr"
print Module_functions.check_num_string(line_list, check_str)
#print out the reading result list
for line in line_list:
    #print "\t".join(line)
    Col1.append(line[0])
    Col5.append(line[4])

print "Check if the column 1 values are unique: "
print Module_functions.allUnique(Col1)

print "Check if the Column 5 are all integers: "
print Module_functions.check_integers(Col5)