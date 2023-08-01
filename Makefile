check_dirs := src

style:
	black $(check_dirs)
	ruff check $(check_dirs) --fix
