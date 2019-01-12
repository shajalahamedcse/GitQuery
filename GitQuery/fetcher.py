class GitTableFetcher:
    """Fetches data from GitHub API, store and return the data in a GitTable."""
    def __init__(self, github):
        self._github = github

    def _Parse(self, label):
        temp = label.split(".")
        if len(temp) == 1:
            return label, None
        else:
            return temp[0], temp[1]
        #print(temp)

    def Fetch(self, label):
        org_name, property_name = self._Parse(label)
        org = self._github.get_organization(org_name)

        if property_name == None:
            print(org)
        elif property_name == "repos":
            repos = org.get_repos()

            for repo in repos:
                print(repo)
        elif property_name == "issues":
            repos = org.get_repos()

            for repo in repos:
                issues = repo.get_issues(state="all")
                for issue in issues:
                    print(issue)