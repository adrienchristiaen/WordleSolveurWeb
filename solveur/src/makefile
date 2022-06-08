##########################
##### COMPILER FLAGS #####
##########################

CFLAGS=-std=c99 -Wall -Wextra -pedantic -fdiagnostics-color=always
CFLAGS+=$(CPPFLAGS) -O0 -g3 -fsanitize=address -fno-omit-frame-pointer -fno-optimize-sibling-calls
LDFLAGS+=-fsanitize=address


############################
##### FILES TO COMPILE #####
############################

# Program:
solveur_test: solveur.o solveur_test.o frequency.o updateList.o delword.o -lm

# Format is:
## program_name: file_name1.o file_name2.o


# Object files
solveur.o: solveur.h solveur.c
solveur_test.o: solveur.h solveur_test.c
frequency.o: solveur.h frequency.c
updateList.o: solveur.h updateList.c
delword.o : solveur.h delword.c

# Format is:
## file_name.o: <dependency.o> <header_file.h> file_name.c


##########################
##### OTHER COMMANDS #####
##########################

clean:
	rm -f *.o *_test

# For the test, replace `linked_list_int_test` with your program name.
test: solveur_test
	./solveur_test

.SILENT: clean