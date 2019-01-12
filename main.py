from GitQuery import core
from GitQuery import fetcher

if __name__ == "__main__":

    token = raw_input()
    sqlserv = core.GitQuery(token)
    f = fetcher.GitTableFetcher(sqlserv._github)
    f.Fetch("google.issues")