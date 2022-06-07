##########################
##### COMPILER FLAGS #####
##########################

CC = cc
CFLAGS = -std=c99 -pedantic -Wall
OBJECTS = frequency_test.o


############################
##### FILES TO COMPILE #####
############################

# Program:
frequency_test: solveur.o frequency.o 

# Format is:
## program_name: file_name1.o file_name2.o


# Object files
solveur.o: solveur.h solveur.c
frequency.o: solveur.h frequency.c 
# Format is:
## file_name.o: <dependency.o> <header_file.h> file_name.c


##########################
##### OTHER COMMANDS #####
##########################

clean:
	rm -f *.o *freqency_test

# For the test, replace `linked_list_int_test` with your program name.
test: frequency_test
	./frequency_test

.SILENT: clean
