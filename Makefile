
all:
	pytest ./ibm_test/ibm_test/tests
	pre-commit run -a

    