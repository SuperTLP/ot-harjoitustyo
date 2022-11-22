from invoke import task

@task
def start(c):
    c.run("poetry run python3 index.py")
@task
def test(c):
    c.run("poetry run pytest src")
@task
def coverage_report(c):
    c.run("poetry run coverage run --branch -m pytest src")
    c.run("poetry run coverage html")
