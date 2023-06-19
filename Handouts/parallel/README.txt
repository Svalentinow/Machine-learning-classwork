The action is in go.sh

This script

1) makes a big file with a lot of rows
2) splits the big file into "numcores" chunks
3) processes each chunk in parallel
4) assembles the chunk parts into one big complete file

For embarassingly parallel tasks this approach gives a "numcores" speedup.

To run the file go.sh try:

$ bash go.sh


