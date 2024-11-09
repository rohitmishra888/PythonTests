from invoke import task

@task
def start(c):
    c.run("python utils/dbcheck.py")

@task
def test(c):
    c.run("pytest Tests/sampletest.py --html=reports.html --self-contained-html --css=pytest-html.css")

