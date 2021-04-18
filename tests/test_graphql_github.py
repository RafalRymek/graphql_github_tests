import pytest
import requests
from hamcrest import assert_that, has_string, is_, greater_than, starts_with, equal_to, not_none
from utils.utils import get_env
from requests_api.queries import user_query, repo_query, rate_limit_query

config_vars = get_env()
headers = {"Authorization": "bearer " + config_vars["access_token"]}


def test_run_bio_query():
    # request
    request = requests.post(url=config_vars["api_url"], json=user_query(login=config_vars["username"]), headers=headers)
    # response
    response = request.json()
    github_user_bio = response["data"]["user"]["bio"]
    print(f"User bio information: {github_user_bio}")
    assert_that(github_user_bio, not_none(), reason="Empty bio")


def test_run_repo_query():
    # request
    request = requests.post(url=config_vars["api_url"], json=repo_query(login=config_vars["username"]), headers=headers)
    # response
    response = request.json()
    github_repo_url = response["data"]["repositoryOwner"]["repository"]["url"]
    print(f"User repository url: {github_repo_url}")
    assert_that(github_repo_url, starts_with("https:"), reason="Wrong url")


def test_run_limit_query():
    # request
    request = requests.post(url=config_vars["api_url"], json=rate_limit_query(), headers=headers)
    # response
    response = request.json()
    github_repo_limit = response["data"]["rateLimit"]["limit"]
    github_repo_remaining = response["data"]["rateLimit"]["remaining"]
    print(f"User rate limit: {github_repo_limit}")
    print(f"User rate remaining: {github_repo_remaining}")
    assert_that(github_repo_limit, is_(equal_to(5000)), reason="Wrong limit")
    assert_that(github_repo_remaining, is_(greater_than(0)), reason="Limit reached")



