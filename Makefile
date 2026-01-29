create-venv:
	uv venv

source-venv:
	source .venv/bin/activate

pcr:
	git add .
	pre-commit run --all-files