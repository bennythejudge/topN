# Problem
Write a program, topN, that given an arbitrarily large file and a number, N, containing individual numbers on each line 
(e.g. 200Gb file), will output the largest N numbers, highest first. 
Tell me about the run time/space complexity of it, and whether you think there's room for improvement in your approach.

# Notes
Idea 1:
- Read the first N numbers into an array while noting the value and index of the smallest of them
- Keep reading another number at a time and:
  - If that number is smaller, ignore it
  - If the number is larger, insert it in place of the previous smallest, and look through the array for the next smallest

Then, at the end, i will have the N largest numbers, but they won’t be sorted. So sort them (descending) in-place using whatever
method is convenient: it won't affect the performance much.

In the worst case, with M numbers in total and where every number in the file is bigger than the previous number, 
I’d have performed around N x M comparisons, because I’d have had to find the next-smallest number out of the N every time 
I saw a new number. That’s not too bad if N is relatively small, and it’s a simple algorithm.

>>> oops: I think I have forgotten the issue of having to find the smallest everytime i find a bigger number than the smallest - that means what exactly? worst case reading once the entire N elements in the array?


Idea 1 alternative:
Sort the first N immediately, note the smallest and largest amongst them, then if a subsequent number was 
in that range, insert it in the sorted position in the array of N, bumping the others along (and losing one). 
>>> here I could use a linked list to be faster? 
Then at the end there’s no sort step to perform.

Idea 2:
implement an external sort 
Found this on stackoverflow:
"The general approach for an external sort is:

```
Read as much data as will fit into an array memory.
Sort it.
Write it out to a temporary file (keeping track of name and size and largest record, etc).
Go back to step 1 until you reach the end of the data.
Set up a merge tree for the files written so that you do the minimum of merges. <<< THIS I DO NOT UNDERSTAND!
Read a line from each of the first (only?) merge phase input files.
Write the smallest (for an ascending sort) to the next temporary file (or the final file).
Get a new record to replace the one just written.
Go back to step 7 until there is no more data to read.
Go back to step 6 to continue the merge until you're done."
```
