#!/usr/bin/env python
import sys


def usage():
  print "Usage: {} <filename> <N>".format(sys.argv[0])

def find_smallest(array):
  smallest = 0
  smallest_at = 0
  for n,i in enumerate(array):
    #print "find_smallest i {} n {}".format(i,n)
    #print "find_smallest Index {} considering {} smallest {} smallest_at {}".format(n,array[n],smallest,smallest_at)
    if n == 0:
      smallest = array[n]
      smallest_at = n
      #print "find_smallest: first time"
    elif array[n] < smallest:
      #print "find_smallest: found {} which is smaller then smallest {}".format(array[n],smallest)
      smallest = array[n]
      smallest_at = n
  #print "find_smallest: returning smallest {} smallest_at {}".format(smallest,smallest_at)
  return smallest, smallest_at
  

def main():
  entries = []
  if len(sys.argv) == 3:
    filename = sys.argv[1]
    N = int(sys.argv[2])
  else:
    usage()
    exit(1)

  # if N is > than ??? maybe it should go for external sort?
  c = 0
  smallest = 0
  smallest_at = 0
  first_time = True
  with open(filename, "r") as f:
    for line in f:
        #print "read {}".format(int(line))
        if first_time:
          #print "first time"
          first_time = False
          smallest = int(line)
          smallest_at = 0
        else: 
            if c<N:
              #print "now loading the {} elements in array and looking for the smallest".format(N)
              entries.append(int(line))
              if int(line) < smallest:
                smallest = int(line)
                smallest_at = c
              #print "smallest {} index {}".format(smallest, smallest_at)
              c += 1
              continue
            else:
                #print "now in the last part of the loop"
                #print "considering read value {} and smallest {}".format(int(line),smallest)
                if int(line) > smallest:
                  #print "found bigger value {}  than smallest {}".format(int(line),smallest)
                  #print "entries before {}".format(entries)
                  entries[smallest_at] = int(line)
                  #print "entries before {}".format(entries)
                  # now find the new smallest
                  #print "before searching the smallest {} {}".format(smallest,smallest_at)
                  smallest, smallest_at = find_smallest(entries)
                  #print "after searching the smallest {} {}".format(smallest,smallest_at)

  f.close()
  print entries
  entries.sort(reverse=True)
  print entries
        

if __name__ == "__main__":
  main()

