from mrjob.job import MRJob
import sys

class CharacterCount(MRJob):
    
    def mapper(self, _, line):
        # Emit each character with count 1
        for char in line:
            yield char, 1
    
    def reducer(self, key, values):
        # Sum up the counts for each character
        yield key, sum(values)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python character_count.py <input_file>")
        sys.exit(1)
    CharacterCount.run()