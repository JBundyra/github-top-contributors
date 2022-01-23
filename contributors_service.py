import requests
import pandas as pd

_GITHUB_BASE_URL = 'https://api.github.com'


def _fetch_complete_github_data(path, github_token):
    current_page = 1
    per_page = 100
    results_count = per_page
    total_results = []

    while results_count == per_page:
        github_url = f'{_GITHUB_BASE_URL}{path}?page={current_page}&per_page={per_page}'

        if github_token is not None:
            headers = {'Authorization': f'token {github_token}'}
            response = requests.get(github_url, headers=headers)
        else:
            response = requests.get(github_url)

        if response.status_code == 200:
            results = response.json()
            results_count = len(results)
            total_results.extend(results)
        else:
            return None

        current_page += 1

    return total_results


def _get_contributions_for_repos(repositories, github_token):
    contributions = []
    for repo in repositories:
        contributors = _fetch_complete_github_data(f'/repos/{repo}/contributors', github_token)
        for contributor in contributors:
            contributions.append({'name': contributor['login'], 'contributions': contributor['contributions']})
    return contributions


def _sum_contributions_by_contributor(repos_contributions):
    contributions_df = pd.DataFrame(repos_contributions)
    total_contributions_by_contributors = contributions_df.groupby(by=['name']).sum()
    sorted_contributions = total_contributions_by_contributors.sort_values(by=['contributions'], ascending=False)
    return sorted_contributions.reset_index().to_dict('records')


def get_contributions_for_organization(organization_name, github_token):
    repositories = _fetch_complete_github_data(f'/orgs/{organization_name}/repos', github_token)
    repo_names = [repo['full_name'] for repo in repositories]
    contributions = _get_contributions_for_repos(repo_names, github_token)
    return _sum_contributions_by_contributor(contributions)
