"""

"""

from github import Github
import json

g = Github("Insert your github OAuth token here")


def getTopCommittees(company_name,m,n):
    q=""
    # search_repositories method uses the github search api
    # performing the search, ordering by number of forks
    repos = g.search_repositories(q,'forks','desc',user=company_name)
    try:
        l = repos.totalCount
    except Exception as e:
        #Error handling if the company does not exist
        message = {"message":"No repository of company with name {}".format(company_name)}
        return json.dumps(message)

    n = min(n,repos.totalCount)
    i=0
    result = []
    #Iterating through the top n repositories
    for repo in repos:
        if(i==n):
            break
        partial_result = {}
        partial_result["repo_name"] = repo.name
        partial_result["committees"] = []

        #Uses the Github API to get the PaginatedList of top contributors to the repo
        contributors = repo.get_contributors()
        m = min(m,contributors.totalCount)
        j=0

        #Iterating through the committees
        for contributor in contributors:
            if j==m:
                break
            c = {}
            c["committee_name"] = contributor.name
            c["commit_count"] = contributor.contributions

            partial_result["committees"].append(c)

            j+=1

        #yield json.dumps(partial_result)
        #Appending the results
        result.append(partial_result)
        i+=1

    return json.dumps(result)

            



if __name__ == '__main__':
    while(True):
        print("Enter the organization name (Enter EXIT to close the program)")
        company_name = input()
        company_name = company_name.lower()
        if company_name == "exit":
            break
        print("Enter the value of n -- number of repositories")
        n = int(input())
        
        print("Enter the value of m -- number of committees per repo")
        m = int(input())
        print(getTopCommittees(company_name,m,n))
        
        

