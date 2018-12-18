
from mrjob.job import MRJob
from mrjob.step import MRStep
import re


class MRExtra(MRJob):

    global fp

    def mapper(self, _, line):
        line = line.lower().split()
        for words in zip(line, line[1:], line[2:]):
            yield list(sorted((words[0], words[1], words[2]))), 1

    def combiner(self, word, counts):
        yield word, sum(counts)
    def reducer(self, key, values):
        yield None, (key, sum(values))
    def Get_only_ten(self, _, wordpairs):
        fp = open('output.txt','w')
        for result in sorted(wordpairs, key=lambda x:x[1], reverse=True)[:10]:
            fp.write(str(result))
            yield result
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                  combiner = self.combiner,
                  reducer=self.reducer),
            MRStep(reducer=self.Get_only_ten)
        ]
if __name__ == '__main__':
    MRExtra.run()