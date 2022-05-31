# Prompt user to ask how many problems they want to solve
echo How many problems do you want to solve today?

read NUM_PROBLEMS

while [ $NUM_PROBLEMS -lt 1 ]
do
    echo That\'s not enough! How many problems do you want to solve today?
    read NUM_PROBLEMS
done

# THE FOLLOWING BELOW IS FOR GMAIL IMPLEMENTATION
# if [ $NUM_PROBLEMS -eq 1 ]
# then
#     echo You will now be asked about this one problem.
# else
#     echo You will be asked about these next few $NUM_PROBLEMS problems.
# fi

echo "What is the target directory for this solution?"

read TARGET_DIR

SUPPORTED_LANGUAGES=("go" "java" "js" "python")

echo Here are all the supported languages.

for language in "${SUPPORTED_LANGUAGES[@]}"
do
    echo $language
done


# Procedure to provide support for user's desired languages.
echo List which of these languages you want to use and press S to save.

read INPUT

while [ "$INPUT" != "S" ]
do
    if [[ " ${SUPPORTED_LANGUAGES[*]} " == *"${INPUT}"* ]];
    then
        echo "Enter a custom path or press ENTER if same as project location."

        read DEST_PATH

        # If no custom path is defined
        if [ "$DEST_PATH" == "" ]
        then
            DEST_PATH="$TARGET_DIR"
        fi

        # Build if the destination path does not yet exist
        if [ ! -d "$DEST_PATH" ]
        then
            mkdir $DEST_PATH
        fi

        # Process language request
        python dependancy_generation.py init $INPUT $DEST_PATH
        echo "Enter another language, or press S to save and exit this process."
        read INPUT
    else
        echo "Language is not supported. Please try again or press S to save and exit this process."
        read INPUT
    fi
done