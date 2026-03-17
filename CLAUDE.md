# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an NVIDIA DLI (Deep Learning Institute) learning path course on training and deploying contact-rich robot manipulation skills using Isaac Lab and Isaac ROS. The course teaches RL-based gear assembly with a UR10e manipulator.

The repository contains **generated static HTML documentation** (the current HEAD has only built output, not source markdown). The original source lives under `docs/` with Sphinx + MyST Parser.

## Build Commands

Requires Python >=3.12 and `uv` package manager.

```bash
# Install dependencies
uv sync

# Build HTML documentation
uv run sphinx-build -M html docs/ docs/_build/

# Serve locally
uv run python -m http.server 8000 -d docs/_build/html/
```

## Architecture

- **Build system**: Sphinx with MyST Parser, NVIDIA Sphinx Theme (`nvidia_sphinx_theme`)
- **Dependencies**: Managed via `pyproject.toml` with `uv`; includes `sphinx-nvlearning` from internal NVIDIA GitLab
- **Binary assets**: Git LFS tracks media files (`.mp4`, `.webm`, `.gif`, `.png`, `.jpg`) and USD files
- **Course structure**: 6 sequential modules — overview, setup, training, validation, deployment, conclusion
- **Source format**: MyST markdown (`.md`) with Sphinx extensions (colon_fence, html_image, attrs, sphinx_design, sphinx_copybutton)
