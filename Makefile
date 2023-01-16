# include .env
# export $(shell sed 's/=.*//' .env)
# export PYTHONPATH=$(CURDIR)/src


install:
	@echo "creating the environment..."
	# @pyenv install 3.10.4
	@pyenv virtualenv 3.10.4 grpc_python
	@pyenv local grpc_python
	@echo "installing grpc libs..."
	pip install -q --no-cache-dir -r requirements.txt
	@echo "OK"

clear:
	@printf "cleaning temp files... "
	@rm -f dist/*.gz
	@rm -rfd *.egg-info
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.log' -delete
	@echo "OK"

protoc:
	python -m grpc_tools.protoc --proto_path=./protos --python_out=. --grpc_python_out=. ./protos/address.proto

serve:
	python server.py
