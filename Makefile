.PHONY: install
install:
	@python -m venv env
	@. env/bin/activate
	@python -m pip install -r requirements.txt

.PHONY: test
test:
	@. env/bin/activate
	@locust -f tests/locustfile.py --host http://localhost:8080
