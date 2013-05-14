__version__ = '0.1a0'
__author__ = 'Martin Natano <natano@natano.net>'


_repository = None
_branch = 'git-orm'
_remote = 'origin'


class GitError(Exception): pass

def set_repository(value):
    from pygit2 import discover_repository, Repository
    global _repository
    try:
        path = discover_repository(value)
    except KeyError:
        raise GitError('no repository found in "{}"'.format(value))
    _repository = Repository(path)


def get_repository():
    return _repository

def set_branch(value):
    global _branch
    _branch = value


def get_branch():
    return _branch

def set_remote(value):
    global _remote
    _remote = value


def get_remote():
    return _remote

def get_config(name):
    repo = _repository
    if repo is None:
        raise GitError('no repository found')
    return repo.config[name]


def is_repo_initialized():
    repo = _repository
    if repo is None:
        return False
    ref = 'refs/heads/{}'.format(_branch)
    try:
        repo.lookup_reference(ref)
    except KeyError:
        return False
    return True


def init_repo():
    import pkg_resources
    from git_orm import transaction

    if is_repo_initialized():
        raise GitError('repository is already initialized')

    with transaction.wrap() as trans:
        tigetrc = pkg_resources.resource_string('tiget', 'data/tigetrc')
        trans.set_blob(['config', 'tigetrc'], tigetrc)
        trans.add_message('Initialize Repository')
