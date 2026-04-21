# Prior CI/CD Experience

**Team:** Collin Schaufele and William Martin

## Relevant Background

This project represents our first formal CI/CD pipeline exercise for CS 3704. Prior hands-on experience with automated builds, testing, and deployment comes primarily from personal and course projects outside the traditional classroom setting.

## Personal Project Experience

### Canvas TUI Reranker (CS 3704 / Independent Project)
- Built a full training pipeline for a Gemma 4 2B reranker model
- Multi-stage setup: SFT (supervised fine-tuning) followed by DPO (Direct Preference Optimization)
- Deployed on a remote Spark GPU cluster with vLLM serving
- Pipeline orchestrated via shell scripts with logging and state tracking across `tmux` sessions
- Scripts: `run_pipeline.py`, `train_student.py`, `path_b_tui.py`, `generate_teacher_preferences.py`

### Canvas TUI
- Python CLI tool wrapping Canvas LMS API
- Pip-installable package (`pip install -e .`) with `pyproject.toml`-based build
- GitHub Actions workflows for auto-assignment, auto-documentation, code coverage, and branch policy
- Multiple workflow files: `ci.yml`, `coverage.yml`, `auto-assign.yml`, `auto-docs.yml`, `branch-policy.yml`
- Coverage threshold enforcement at 80%

### OpenClaw (Home Lab Automation)
- Personal home server running Linux with a multi-agent automation system (OpenClaw)
- Agent orchestration with task scheduling (`oc-tasks`), heartbeat monitoring, and calendar integration
- Deployed via `systemd` services, managed over SSH
- Configuration stored in JSON with a staged-apply workflow for safe changes

### Spark GPU Cluster
- Remote headless Ubuntu server running Spark for model inference and training
- Models served via `vLLM` with a custom `forge` CLI tool for model lifecycle management (load/unload/swap)
- VRAM-aware scheduling across multiple model slots
- Models: Gemma 4 31B, Gemma 4 2B, Nemotron-Super 120B, Qwen 3 variants

## Tools We Have Used

| Category | Tools |
|----------|-------|
| Version Control | Git, GitHub (forks, PRs, branches, code review) |
| CI/CD | GitHub Actions, `pytest`, coverage reports |
| Python Packaging | `pip`, `setuptools`, `pyproject.toml` |
| Deployment | SSH, `systemd`, Flask dev server, vLLM |
| Infrastructure | Spark GPU cluster, `tmux`, `forge` CLI |
| Automation | Shell scripts, cron jobs, OpenClaw agents |

## Course Integration

This assignment (Top Five GitHub Actions) applies the CI/CD concepts from CS 3704 in a structured way. The workflow demonstrates:
- Automated testing on every push/PR
- Python environment setup via `actions/setup-python`
- Multi-job pipeline (build + lint)
- Pull request integration

## Questions About CI/CD

1. What is the difference between a `push` trigger and a `pull_request` trigger in terms of what code the workflow sees?
2. How do GitHub Actions secrets work, and when should you use them vs. public variables?
3. Is it better to have one large workflow file or many small ones? What are the tradeoffs?
4. How would you handle CI/CD for a project that requires GPU resources (e.g., model training)?
