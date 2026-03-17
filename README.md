# PROJECT_NAME

## Configuration

### uv
This repository uses [uv](https://docs.astral.sh/uv/) for dependency management. If you're new to uv, you don't need to know much more than the commands we use in the [build instructions](#How-to-Build). We recommend [installing uv](https://docs.astral.sh/uv/getting-started/installation/).

### Git LFS
This repository uses Git Large File Storage to store images, videos, and USD content. To ensure a frictionless process, make sure you have it installed before cloning the repository.

**Install:**
```
git lfs install
```

## How to Build
1. `uv run sphinx-build -M html docs/ docs/_build/`
1. `uv run python -m http.server 8000 -d docs/_build/html/`
1. In a web browser, open `http://localhost:8000`

## Update sphinx-nvlearning
```
uv add sphinx-nvlearning --upgrade-package sphinx-nvlearning
```