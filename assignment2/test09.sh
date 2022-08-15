#!/bin/dash

# ==============================================================================
# test08.sh
# Test the slippy function
#
# Written by: Jinming Liu <z5373811@unsw.edu.au>
# Date: 2022-08-7
# For COMP2041/9044 Assignment 2
# ==============================================================================

# add the current directory to the PATH so scripts
# can still be executed from it after we cd
PATH="$PATH:$(pwd)"

# Create a temporary directory for the test.
test_dir="$(mktemp -d)"
cd "$test_dir" || exit 1

# Create some files to hold output.

expected_output="$(mktemp)"
actual_output="$(mktemp)"

# Remove the temporary directory when the test is done.

trap 'rm "$expected_output" "$actual_output" -rf "$test_dir"' INT HUP QUIT TERM EXIT

# create a sequence from 10 to 100 and use slippy d and p command to deal with
cat > "$expected_output" <<EOF
30
31
33
34
35
36
37
38
39
40
41
43
EOF

seq 24 43 | slippy '/2/d # delete  ;  4  q # quit' > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0