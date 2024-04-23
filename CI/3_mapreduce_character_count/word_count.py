from mrjob.job import MRJob
import re
import sys

WORD_RE = re.compile(r"[\w']+")

class WordCount(MRJob):
    
    def mapper(self, _, line):
        # Emit each word with count 1
        for word in WORD_RE.findall(line):
            yield word.lower(), 1
    
    def reducer(self, key, values):
        # Sum up the counts for each word
        yield key, sum(values)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <input_file>")
        sys.exit(1)
    WordCount.run()