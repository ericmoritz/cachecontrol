from invoke import run, task


VENV = 'venv'


def env_do(tail, **kw):
    return run('%s/bin/%s' % (VENV, tail), **kw)


@task
def virtualenv():
    run('virtualenv %s' % VENV)


@task('virtualenv')
def bootstrap():
    env_do('pip install -r dev_requirements.txt')


@task
def clean_env():
    run('rm -r venv')


@task
def test_all():
    env_do('tox')


@task
def docs():
    run('cd docs && make html')


@task
def release(part):
    env_do('bumpversion %s' % part)
    run('git push origin master')
    run('git push --tags origin master')
    env_do('python setup.py sdist upload')
