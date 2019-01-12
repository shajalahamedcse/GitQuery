class GitTableFetcher:
    """Fetches data from GitHub API, store and return the data in a GitTable."""
    def __init__(self, github):
        self._github = github

    def _Parse(self, label):
        temp = label.split(".")
        print(temp)