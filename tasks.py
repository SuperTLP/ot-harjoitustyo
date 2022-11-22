from invoke import task

@task
def start(c):
    c.run("python3 src/index.py")
@task
def test(c):
    c.run("pytest src")
@task
def coverage_report(c):
    c.run("coverage run --branch -m pytest src")
    c.run("coverage html")
