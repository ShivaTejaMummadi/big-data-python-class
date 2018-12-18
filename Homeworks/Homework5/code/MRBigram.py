
#saving the code to a file

from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MRBigram(MRJob):

    #mapper method
    def mapper(self, _, line):
        line = line.lower().split()
        for words in zip(line, line[1:]):
            yield list((words[0], words[1])), 1

    #combiner method
    def combiner(self, word, counts):
        yield word, sum(counts)
        
    #reducer method
    def reducer(self, key, values):
        yield None, (key, sum(values))
        
    #reducer2 method which only gets sorted top 10
    def Get_only_ten(self, _, wordpairs):
        for result in sorted(wordpairs, key=lambda x:x[1], reverse=True)[:10]:
            yield result
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                  combiner = self.combiner,
                  reducer=self.reducer),
            MRStep(reducer=self.Get_only_ten)
        ]
if __name__ == '__main__':
    MRBigram.run()