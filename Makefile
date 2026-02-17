install:
	uv sync


VD-games:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check games_project_Harlamova/VD_games
