                                -=} Git ORM {=-
                          Git Object-Relational Mapper


Git-orm provides a django model like interface for storing objects in a git
repository.


INSTALLATION:

Compile libgit2[1] from source or install it via your distributions package
manager. Currently git-orm is tested with libgit2 version 0.20.0.
Afterwards execute the setup script (root permissions might be needed):

    $ ./setup.py install


USAGE:

    from datetime import datetime

    from git_orm import models, set_repository, set_branch, transaction
    from git_orm.models import Q


    # define your model here
    class Article(models.Model):
        title = models.TextField()
        text = models.TextField()
        published_at = models.DateTimeField(null=True)


    set_repository('/path/to/your/git/repo')
    set_branch('feature_branch_xy')

    # let's create an article
    article = Article(title='Using git-orm is easy!')
    article.text = ...
    article.save()

    # or create two articles in one commit
    with transaction.wrap():
        Article.objects.create(...)
        Article.objects.create(...)

    # query syntax is similar to the one from django
    article = Article.objects.get(title__contains='easy')

    # advanced querying is also possible
    Article.objects.filter(Q(title__contains='easy') | Q(text__icontains='hard'))

    # timestamps are provided automatically
    article.created_at
    article.updated_at


HACKING:

PEP 8[2] should be followed for every new code.
An exception to this rule is when creating custom exceptions (no pun intended).
The pass keyword should appear on the same line as the class keyword when no
methods are overwritten in the subclass. So multiple custom exceptions may be
declared without wasting screen space.
e.g.:

    class FrobnicationNotPossible(Exception): pass
    class IDontWantToDoThis(Exception): pass

Automatic style checking and detection of common errors is possible with pep8
and pyflakes. Both tools are available on pypi.

When hacking on git-orm you can install it in development mode.

    $ ./setup.py develop

Development mode allows to change the source code without reinstalling the
package.

Please run the test suite before opening a pull request or committing in the
master branch.

    $ ./setup.py nosetests

Every non-trivial code should have according tests.


AUTHORS & CONTRIBUTORS:

Martin Natano <natano@natano.net>
Andreas Kopecky <andreas.kopecky@gmail.com>


[1] https://github.com/libgit2/libgit2
[2] http://www.python.org/dev/peps/pep-0008/
