#!/usr/bin/python

# from pygithub3 import Github

from git import *
from sh import git

def dump(obj):
    for attr in dir(obj):
        if hasattr( obj, attr ):
            print( "obj.%s = %s" % (attr, getattr(obj, attr)))

# gh = Github(login='user', password='pass')
#
# integralads = gh.orgs.get('integralads')
#
# dump(integralads)
# integraladsrepo = integralads.repos.list().all()
# print integraladsrepo

from github import Github

g = Github("user", "pass")

integral = g.get_organization("integralads")
repo = 'niagara'

pull_number = 257

pull_request = integral.get_repo(repo).get_pull(pull_number)

base =  pull_request.base.ref

head = pull_request.head.ref #.base.ref

repo = Repo(".")
repo.remote("origin").fetch()

# repo.git.checkout('head', b = 'origin/{0}'.format(head))
# dump(repo.remote("origin").refs[head])#.checkout()

# g.checkout("origin/no-join-cassandra")
# print (repo.remote("origin").refs["no-join-cassandra"])
git.checkout(base)
# for s in integral.plan.private_repos:
    # dump(s)

    # print repo.name
    # repo.edit(has_wiki=False)
