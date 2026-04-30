.DEFAULT_GOAL := help
help:
	@echo "This makefile for repo-level activity"

create-practice:
ifndef PRACTICE
	${error must pass val via PRACTICE}
endif
	@echo "Creating practice"
	mkdir -p ${PRACTICE}
	cp PracticeMakefile ${PRACTICE}/Makefile

remove-practice:
ifndef PRACTICE
	${error must pass val via PRACTICE}
endif
	@echo "Deleting practice"
	rm -rf ${PRACTICE}

#mkdir demo-practice
#mkdir demo-practice/src
#mkdir demo-practice/tests
#mkdir demo-practice/docs
#touch demo-practice/README.md

PORT1 ?= 8001
PORT2 ?= 8002
uvicorn-run:
	cd product_service && poetry run uvicorn src.app.main:app --host 127.0.0.1 --port ${PORT1} &
	cd order_service && poetry run uvicorn src.app.main:app --host 127.0.0.1 --port ${PORT2}