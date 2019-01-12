from github import Github

class GitQuery:
    """Meta Components for Github"""
    def __init__(self, token):
        self._github = Github(token)

