#!/bin/bash 

echo "Beginning to sort now."

python auto_batchfilegenerator_W186.py 1
#./sorting W186_autobatch_sirius001.batch #"${arr[@]}"}

declare -a arr=("000" "001" "002" "003" "004" "005" "006" "007" "008" "009" "010" "011" "012" "013" "014" "015" "016" "017" "018" "019" "020" "021" "022" "023" "024" "025" "026" "027" "028" "029" "030" "031" "032" "033")
#declare x = 0
for x in {0..33}
do
python auto_batchfilegenerator_W186.py "$x" 
echo "$x"
echo "${arr["$x"]}"
./sorting W186_autobatch_sirius${arr[$x]}.batch
done

echo "Done!"
