import csv
from timing import timing


# using yield to reduce memory usage
def yield_lines(csv_file):
    for line in csv_file:
        yield line


def diff_list(list1, list2):
    # the "*" is list expansion, makes for a prettier print
    print("In list 1 but not in list 2:\n{}".format(*list(set(list1) - set(list2))))
    print("In list 2 but not in list 1:\n{}".format(*list(set(list2) - set(list1))))


@timing
def compare_rows_with_yield(file1, file2):
    print("Line by line comparison")
    print("Lines in file 1 but not in file 2:\n{}".format(*compare_rows_line_by_line(file1, file2)))
    print("Lines in file 2 but not in file 1:\n{}".format(*compare_rows_line_by_line(file2, file1)))


# use yield, for very large files this is much more memory efficient, lambda I believe charges by memory usage
def compare_rows_line_by_line(file1, file2):
    in_f1_not_f2 = []
    with open(file1) as f1, open(file2) as f2:
        # compare each line of the first csv to every line of the second, if doesn't exist store it
        for line_f1 in yield_lines(f1):
            found = False
            if not found:
                for line_f2 in yield_lines(f2):
                    if line_f1 == line_f2:
                        found = True
                    break
            if not found:
                in_f1_not_f2.append(line_f1)
    f1.close(), f2.close()
    return in_f1_not_f2


@timing
def compare_columns(file1, file2):
    # open both files
    with open(file1) as f1, open(file2) as f2:
        # create a reader object for each file
        csv_reader1 = csv.reader(f1, delimiter=',') 
        csv_reader2 = csv.reader(f2, delimiter=',')
        # .next gets the first line which are the column names, pass both to the diff function
        diff_list(csv_reader1.next(), csv_reader2.next())
        # return file handles
        f1.close(), f2.close()


# diff both files in memory, might be faster but very memory spendy
@timing
def compare_rows_both_in_memory(file1, file2):
    with open("file1.csv") as f1, open("file2.csv") as f2:
        list1 = [x for x in f1]
        list2 = [x for x in f2]
        print("Both in memory")
        diff_list(list1, list2)
        

def main():
    compare_columns('file1.csv', 'file2.csv')
    compare_rows_with_yield('file1.csv', 'file2.csv')
    compare_rows_both_in_memory('file1.csv', 'file2.csv')


if __name__ == "__main__":
    # execute only if run as a script
    main()
