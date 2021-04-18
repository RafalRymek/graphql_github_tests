# Bootcamp GrpaahQL automated tests
Automated API tests to cover endpoints from GitHUb using GraphQL

Following tech stack is using:
python   
pytest 

# Setup:
1. open terminal
2. run `git clone https://github.com/RafalRymek/graphql_github_tests` to clone repository   
3. run `cd graphql_github_tests` to move to local repository folder  
4. run `cp config.json.example config.json` to create config.json file
5. add actual parameters (access_token, username) of test users to config.json file
6. run `pipenv install` to set up all necessary dependencies from Pipfile.lock  
7. run `pipenv shell` to be able to use all pipenv dependencies from terminal

#  Execution:

to run graphql tests with pytest:
1. previously should create your own access token to authorization to GitHub 
   `https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)`
5. run `export PYTHONPATH=`pwd`     
6. run `pytest tests/test_graphql_github.py`

