#!/bin/dash

# ==============================================================================
# test08.sh
# Test the tigger-init and tigger-add command and tigger-show command.
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

# Create tigger repository

cat > "$expected_output" <<EOF
Initialized empty tigger repository in .tigger
EOF

tigger-init > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# Create simple files.

echo "1" > a
echo "2" > b


# add files to the repository staging area
tigger-add a


# Check that files that has been commited

cat > "$expected_output" <<EOF
Committed as commit 0
EOF

tigger-commit -m "first commit" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# Modify files
echo 3 >c
echo 4 >d

# add files to the repository staging area
tigger-add c d


#remove a c from index
tigger-rm --cached  a c

# Check tigger-rm command

cat > "$expected_output" <<EOF
Committed as commit 1
EOF

tigger-commit -m "second commit" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


# Check tigger-show command

cat > "$expected_output" <<EOF
1
EOF


tigger-show 0:a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


# Check tigger-show command

cat > "$expected_output" <<EOF
tigger-show: error: 'a' not found in commit 1
EOF


tigger-show 1:a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# Check tigger-show command

cat > "$expected_output" <<EOF
tigger-show: error: 'a' not found in index
EOF


tigger-show :a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0