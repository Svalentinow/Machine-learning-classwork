python3 make_big_file.py
num_lines=$(wc -l < big_file.csv)
echo "file is $num_lines long"
chunksize=$(expr $num_lines / 16)
numcores=16
echo "with $numcores cores splitting into files with $chunksize lines"
split -l $chunksize big_file.csv chunk
for file in chunk*;
do 
    python3 process_small_file.py $file &
done
wait;
cat out_chunk* > big_file_prime.csv
rm chunk*
rm out_chunk*


