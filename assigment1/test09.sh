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
touch a b

# add files to the repository staging area
tigger-add a b


# Check that files that has been commited

cat > "$expected_output" <<EOF
Committed as commit 0
EOF

tigger-commit -m "first commit" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# remove file a
rm a


# Check that files that has been commited

cat > "$expected_output" <<EOF
nothing to commit
EOF

tigger-commit -m "second commit" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# add files to the repository staging area
tigger-add a


# Check that files that has been commited

cat > "$expected_output" <<EOF
Committed as commit 1
EOF

tigger-commit -m "second commit" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

#remove file b from index
tigger-rm --cached b


# Check that files that has been commited

cat > "$expected_output" <<EOF
Committed as commit 2
EOF

tigger-commit -m "second commit" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

#remove file b from index and working space
cat > "$expected_output" <<EOF
tigger-rm: error: 'b' is not in the tigger repository
EOF

tigger-rm b > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

#add file b to index
tigger-add b

#Check the tigger-rm command
cat > "$expected_output" <<EOF
tigger-rm: error: 'b' has staged changes in the index
EOF

tigger-rm b > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


# Check that files that has been commited

cat > "$expected_output" <<EOF
Committed as commit 3
EOF

tigger-commit -m "third commit" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

#remove file b from index and working space
tigger-rm b


#Check the tigger-rm command
cat > "$expected_output" <<EOF
Committed as commit 4
EOF

tigger-commit -m "fourth commit" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0