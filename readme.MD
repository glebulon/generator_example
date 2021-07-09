# csv_script

A script that takes 2 csv files and prints out the different headers between them and the different rows between them.

Script was run and tested using python 2.7 on windows10

## Installation

Only package required is csv

```bash
pip install csv
```

## Usage

```
python .\csv_script.py
```

## Memory usage

Testing out 2 ways of going through the csv file, one by loading everything into memory, second by using yield to create a generator and go through line by line shows the memory footprints of both methods

```
python -m memory_profiler .\csv_script.py

Line #    Mem usage    Increment   Line Contents
================================================
    13   21.242 MiB   21.242 MiB   @profile
    14                             def compare_rows_with_yield(file1, file2):
    15   21.242 MiB    0.000 MiB       print("Line by line comparison")
    16   21.367 MiB    0.125 MiB       print("Lines in file 1 but not in file 2: {}".format(compare_rows_line_by_line(file1, file2)))
    17   21.434 MiB    0.066 MiB       print("Lines in file 2 but not in file 1: {}".format(compare_rows_line_by_line(file2, file1)))


Filename: .\csv_script.py

Line #    Mem usage    Increment   Line Contents
================================================
    51   21.434 MiB   21.434 MiB   @profile
    52                             def compare_rows_both_in_memory(file1, file2):
    53   21.434 MiB    0.000 MiB       with open("file1.csv") as f1, open("file2.csv") as f2:
    54                                     # create a reader object for each file
    55   21.434 MiB    0.000 MiB           csv_reader1 = csv.reader(f1, delimiter=',')
    56   21.434 MiB    0.000 MiB           csv_reader2 = csv.reader(f2, delimiter=',')
    57  175.215 MiB    0.449 MiB           list1 = [x for x in f1]
    58  327.305 MiB    0.445 MiB           list2 = [x for x in f2]
    59  327.305 MiB    0.000 MiB           print("Both in memory")
    60  327.559 MiB    0.254 MiB           diff_list(list1, list2)
    
 ```
 
 ## Execution speed
 ```
 Elapsed time for compare_rows_with_yield: 3.80500006676
 Elapsed time for compare_rows_both_in_memory: 2.80399990082
 ```