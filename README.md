# DNA Identifier

A Python program that identifies a person from a DNA sequence.

## How it works
1. Reads a CSV database with `csv.DictReader`. The header tells the program
   which short repeating sequences (STRs) to count, so nothing is hard-coded.
2. Reads a DNA sequence from a text file.
3. For each STR, `longest_match` finds the longest run of consecutive repeats.
4. Compares the counts to every person in the database and prints the name
   of the person who matches on all of them, or `No match`.

## Usage
    python dna.py databases/large.csv sequences/5.txt

## Testing
I tested `longest_match` by itself on hand-made strings (e.g. AGATAGAT -> 2,
AGATCAGAT -> 1, empty string -> 0) before connecting it to the rest, and then
ran all five small-database sequences and check50.

## If two people match
The program currently prints the first match. For a database where two people
could match, I would collect all matches and print every name (or report that
the result is ambiguous), and suggest adding more STRs to tell them apart.
