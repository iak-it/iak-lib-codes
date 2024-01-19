import nox
from nox.sessions import Session


nox.options.sessions = (
    "black",
    "flake8",
    "pylint",
    "mypy",
    "black_tests",
    "flake8_tests",
    "pylint_tests",
    "mypy_tests",
    "tests",
)


@nox.session(python=False)
def black(session: Session) -> None:
    session.run("black", "src", "--line-length=78")


@nox.session(python=False)
def flake8(session: Session) -> None:
    session.run("flake8", "src")


@nox.session(python=False)
def pylint(session: Session) -> None:
    session.run("Pylint", "src", "--rc-file", ".config/.pylintrc")


@nox.session(python=False)
def mypy(session: Session):
    session.run("mypy", "src", "--config", ".config/.mypy.ini")


@nox.session(python=False)
def black_tests(session: Session) -> None:
    session.run("black", "tests", "--line-length=78")


@nox.session(python=False)
def flake8_tests(session: Session) -> None:
    session.run("flake8", "tests")


@nox.session(python=False)
def pylint_tests(session: Session) -> None:
    session.run("Pylint", "tests", "--rc-file", ".config/.pylintrc")


@nox.session(python=False)
def mypy_tests(session: Session):
    session.run("mypy", "tests", "--config", ".config/.mypy.ini")


@nox.session(python=False)
def tests(session: Session) -> None:
    session.run("pytest", "tests")
