# Prompt user to ask how many problems they want to solve
echo How many problems do you want to solve today?

read NUM_PROBLEMS

while [ $NUM_PROBLEMS -lt 1 ]
do
    echo That\'s not enough! How many problems do you want to solve today?
    read NUM_PROBLEMS
done

if [ $NUM_PROBLEMS -eq 1 ]
then
    echo You will now be asked about this one problem.
else
    echo You will be asked about these next few $NUM_PROBLEMS problems.
fi

SRC_DIR=src

cd $SRC_DIR
python3 quickstart.py
cd ..