import csv
import sys


def main():
    # Need exactly 2 arguments (plus the program name itself = 3 total)
    if len(sys.argv) != 3:
        print("Usage: python dna.py DATABASE.csv SEQUENCE.txt")
        sys.exit(1)

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Read the database. Each row becomes a dictionary like {"name": "Alice", "AGATC": "2", ...}
    with open(database_file) as f:
        reader = csv.DictReader(f)
        name_column = reader.fieldnames[0]   # first column is the name
        chunks = reader.fieldnames[1:]       # the rest are the DNA chunks (not hard-coded!)
        people = list(reader)

    # Read the DNA file as one long string
    with open(sequence_file) as f:
        dna = f.read().strip()

    # Count the longest run of each chunk in the DNA
    counts = {}
    for chunk in chunks:
        counts[chunk] = longest_match(dna, chunk)

    # Compare with each person. CSV values are text, so convert to int.
    for person in people:
        if all(int(person[chunk]) == counts[chunk] for chunk in chunks):
            print(person[name_column])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Return the longest run of consecutive repeats of subsequence in sequence."""
    longest = 0
    length = len(subsequence)

    # Try starting a run at every position in the DNA
    for i in range(len(sequence)):
        count = 0

        # Jump forward one chunk at a time while the chunk keeps matching
        while sequence[i + count * length : i + (count + 1) * length] == subsequence:
            count += 1

        # Remember the best streak so far
        if count > longest:
            longest = count

    return longest


main()
