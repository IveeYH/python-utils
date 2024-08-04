#!/bin/bash

# Function to read parameters from YAML and prompt for input
get_parameters() {
    local util_dir=$1
    local param_file="$util_dir/parameters.yaml"

    if [ ! -f "$param_file" ]; then
        echo "No parameters.yaml file found in $util_dir."
        return 1
    fi

    # Use yq to parse the yaml file
    # Ensure you are using the correct yq syntax for your version
    # This assumes mikefarah/yq version 4.x
    params=$(yq eval '.parameters | keys | .[]' "$param_file")

    if [ -z "$params" ]; then
        echo "No parameters found in $param_file."
        return 1
    fi

    echo "Please provide the following parameters for $util_dir:"

    # Iterate over each parameter and prompt the user for input
    for param in $params; do
        description=$(yq eval ".parameters.$param.description" "$param_file")
        
        # Check if description is found, if not, set a default value
        if [ -z "$description" ]; then
            description="No description available."
        fi
        
        read -p "$param ($description): " value
        export "$param"="$value"
    done

    return 0
}

# List all directories containing utilities
echo "Available utilities:"
utils=()
for dir in */ ; do
    # Check if the directory contains a main.py file
    if [ -f "$dir/main.py" ]; then
        utils+=("$dir")
        echo "${#utils[@]}. ${dir%/}"
    fi
done

# Prompt the user to choose a utility
read -p "Enter the number of the utility you want to use: " choice

# Check if the choice is valid
if [ -z "${utils[$choice-1]}" ]; then
    echo "Invalid choice. Exiting."
    exit 1
fi

# Get the chosen utility directory
chosen_util="${utils[$choice-1]}"
echo "You chose $chosen_util."

# Get parameters for the chosen utility
if get_parameters "$chosen_util"; then
    echo "Running $chosen_util/main.py with the provided parameters..."

    # Construct the command to run the main.py script with the parameters
    params=$(yq eval '.parameters | keys | .[]' "$chosen_util/parameters.yaml")
    param_args=""

    for param in $params; do
        # Use indirect variable expansion to access the variable value
        value="${!param}"
        param_args="$param_args --$param \"$value\""
    done

    # Execute the script with parameters
    eval python3 "$chosen_util/main.py" $param_args
else
    echo "Failed to get parameters. Exiting."
    exit 1
fi