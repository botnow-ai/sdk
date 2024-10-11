#!/bin/bash

# List of directories to exclude (relative to the root of your proto directory)
EXCLUDE_DIRS=("")

# Construct the find command with excluded directories
FIND_CMD="find protos -name '*.proto'"

for DIR in "${EXCLUDE_DIRS[@]}"; do
  FIND_CMD="$FIND_CMD -not -path '$DIR/*'"
done

# Execute the find command and pass the results to xargs for protoc compilation
eval "$FIND_CMD" | xargs poetry run python -m grpc_tools.protoc -Iprotos \
  --python_out=sdk/pb --pyi_out=sdk/pb --grpc_python_out=sdk/pb
