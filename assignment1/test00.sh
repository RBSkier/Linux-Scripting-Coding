#!/bin/dash

# ==============================================================================
# test00.sh
# Test the tigger-init
#
# Written by: Jinming Liu <z5373811@unsw.edu.au>
# Date: 2022-07-11
# For COMP2041/9044 Assignment 1
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

# Create a .tigger directory.

mkdir .tigger


# Create tigger repository

cat > "$expected_output" <<EOF
tigger-init: error: .tigger already exists
EOF

tigger-init > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0
