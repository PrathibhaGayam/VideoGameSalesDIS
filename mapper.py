#!/usr/bin/python

# Format of each line is:
# name\tplatform\tyear\tgenre\tpublisher\tnasales\teusales\tjpsales\tothersales\tglobalsales\tcriticScore\tcriticCount\tuserScore\tuserCount\tdeveloper\trating
#
# We want elements 4 (genre) and 6+7+8+9+10 (asales+eusales+jpsales+othersales+globalsales)
# We need to write them out to standard output, separated by a tab

import sys

salesTotal = 0.0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 16:
        name, platform, year, genre, publisher, nasales, eusales, jpsales, othersales, globalsales, criticScore, criticCount, userScore, userCount, developer,rating = data
	salesTotal = float(nasales)+ float(eusales)+ float(jpsales)+ float(othersales)+ float(globalsales)
        print "{0}\t{1}".format(year, salesTotal)

