#!/bin/bash
set -e
echo "--- Checking Scope of Changes ---"
TEST_DIR="tests/"
run_all="false"

target_branch="origin/${GITHUB_BASE_REF}"
merge_base=$(git merge-base "$target_branch" HEAD)

echo "Comparing HEAD against merge base ($merge_base) with target $target_branch"

if ! git diff --quiet --exit-code "$merge_base" HEAD; then
  echo "Changes detected. Analyzing location..."
  while IFS= read -r file; do
    trimmed_file=$(echo "$file" | xargs)
    if [[ -n "$trimmed_file" && ! "$trimmed_file" == "$TEST_DIR"* ]]; then
      echo "  Change outside '$TEST_DIR' found: '$trimmed_file'. Flagging to run all tests."
      run_all="true"
      break
    fi
  done < <(git diff --name-only "$merge_base" HEAD)

  if [[ "$run_all" == "false" ]]; then
    echo "  All changes are within '$TEST_DIR'. Flagging to run picked tests."
  fi
else
  echo "No changes detected compared to merge base."
  run_all="false"
fi

echo "Setting output: run_all_tests=$run_all"
echo "run_all_tests=$run_all" >> "$GITHUB_OUTPUT"

echo "--- Scope check finished ---"