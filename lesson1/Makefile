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