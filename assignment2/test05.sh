#!/bin/dash

# ==============================================================================
# test05.sh
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

# create a sequence from 10 to 100 and use slippy s command to deal with
cat > "$expected_output" <<EOF
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
-02
103
104
105
106
107
108
109
110
EOF

seq 77 110 | slippy '/1.2/s/1/-/g' > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0