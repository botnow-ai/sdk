prepare-python:
	echo "install poetry"
	pip install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple
	echo "install grpc tools"
	poetry install

.PHONY: prerequisites
prerequisites: prepare-python

.PHONY: protos-gen-py
protos-gen-py:
	@echo "generate python protos"
	@sh scripts/protoc_python.sh
	@echo "replace import path"
	@sh scripts/replace-import-path.sh


.PHONY: protos-gen
protos-gen: protos-gen-py


.PHONY: install
install:
	poetry lock --no-update
	poetry install
.PHONY: pylint
pylint:
	@poetry run pylint -d all -e E0602 ./
	@poetry run black .