import os
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> str:
    """Execute a command and return its stdout.

    Args:
        cmd: Command and arguments.
        cwd: Working directory for the subprocess.

    Returns:
        Captured standard output stripped of trailing whitespace.
    """

    res = subprocess.run(cmd, cwd=cwd, check=True, stdout=subprocess.PIPE, text=True)
    return res.stdout.strip()


def run_installed(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Install bumpwright and execute a CLI command.

    This helper creates an isolated virtual environment, installs the
    current repository into it using ``pip install .``, and then runs the
    provided command within that environment. It ensures the published
    ``bumpwright`` console script behaves correctly when invoked.

    Args:
        cmd: Command to execute, typically beginning with ``"bumpwright"``.
        cwd: Working directory for the subprocess.

    Returns:
        The completed process capturing both standard output and error.
    """

    with tempfile.TemporaryDirectory() as venv_dir:
        # Create a virtual environment with pip available.
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
        bin_dir = Path(venv_dir) / ("Scripts" if os.name == "nt" else "bin")

        # Install the current repository into the virtual environment.
        subprocess.run(
            [bin_dir / "pip", "install", "."],
            cwd=Path(__file__).resolve().parents[1],
            check=True,
        )

        env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"}

        # Execute the command inside the prepared environment.
        return subprocess.run(
            cmd,
            cwd=cwd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )


def setup_repo(tmp_path: Path, *, version: str = "0.1.0", scheme: str | None = None) -> tuple[Path, Path, str]:
    """Create a git repository with a minimal Python project.

    Args:
        tmp_path: Temporary directory provided by pytest.
        version: Initial project version written to ``pyproject.toml``.
        scheme: Optional versioning scheme recorded in ``bumpwright.toml``.

    Returns:
        Tuple of repository path, package path, and base commit hash.
    """

    repo = tmp_path / "repo"
    repo.mkdir()
    run(["git", "init"], repo)
    run(["git", "config", "user.email", "a@b.c"], repo)
    run(["git", "config", "user.name", "tester"], repo)

    (repo / "pyproject.toml").write_text(
        f"""[project]\nname = 'demo'\nversion = '{version}'\n""",
        encoding="utf-8",
    )
    pkg = repo / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("def foo() -> int:\n    return 1\n", encoding="utf-8")

    config = "[project]\npublic_roots=['pkg']\n"
    if scheme:
        config += f"[version]\nscheme='{scheme}'\n"
    (repo / "bumpwright.toml").write_text(config, encoding="utf-8")

    run(["git", "add", "."], repo)
    run(["git", "commit", "-m", "base"], repo)
    base = run(["git", "rev-parse", "HEAD"], repo)
    return repo, pkg, base
