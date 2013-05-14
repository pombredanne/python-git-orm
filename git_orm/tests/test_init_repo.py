from nose.tools import *

from git_orm.testcases import GitTestCase
from git_orm import init_repo, GitError


class TestInitRepo(GitTestCase):
    def test_init_repo(self):
        init_repo()
        try:
            self.repo.lookup_reference(self.branchref)
        except KeyError:
            self.fail('{} does not exist'.format(self.branchref))
        self.assert_commit_count(1)
        self.assert_file_exists('config/tigetrc')

    def test_already_initialized(self):
        init_repo()
        assert_raises(GitError, init_repo)
