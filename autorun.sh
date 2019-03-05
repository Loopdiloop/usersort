#!/bin/bash 

echo "Beginning to sort now."

echo "Removing old files"
rm fileinfo.txt
rm W186_autobatch_sirius*.batch
rm 186W_autogenerated_*.root
declare -a arr=("000" "001" "002" "003" "004" "005" "006" "007" "008" "009" "010" "011" "012" "013" "014" "015" "016" "017" "018" "019" "020" "021" "022" "023" "024" "025" "026" "027" "028" "029" "030" "031" "032" "033")
# For x range 0 -> 33
for x in {0..33}
do
echo "$x"
python auto_batchfilegenerator_W186.py "$x" 
./sorting W186_autobatch_sirius${arr[$x]}.batch
done

#echo "Removing auto batchfiles"
#rm W186_autobatch_sirius*.batch

echo "Done!"
