check_dirs := src notebooks

style:
	black $(check_dirs)
	ruff check $(check_dirs) --fix