def user_query(login):
    return {
        "query": """query {
    user(login: "%s") {
    bio
    bioHTML
    createdAt
    company
    avatarUrl
    }
    }
    """
                 % login
    }


def repo_query(login):
    return {
        "query": """query {
    repositoryOwner(login: "%s") 
    {
      repository(name: "bootcamp_3_api_tests") {
        url
        } 
    } 
    } 
    """
                 % login
    }


def rate_limit_query():
    return { "query": """
{
  viewer {
    login
    createdAt
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""}
