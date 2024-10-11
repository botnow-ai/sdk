#!/bin/bash

# 定义存储生成文件的目录
BASE_DIR="sdk/pb"

os_name=$(uname)
# 查找所有 *_grpc.py 文件
for file in $(find $BASE_DIR -name '*.py'); do
    # 根据操作系统选择 sed 命令
    if [ "$os_name" = "Darwin" ]; then
      # 使用 sed 更新 from xxx import *_pb2 的 import 语句，增加 base.pb. 前缀
      sed -i '' 's/from \(.*\) import \(.*_pb2\)/from sdk\.pb\.\1 import \2/' "$file"
    else
      sed -i 's/from \(.*\) import \(.*_pb2\)/from sdk.pb.\1 import \2/' "$file"
    fi
done

echo "Updated imports in *_grpc.py files."

