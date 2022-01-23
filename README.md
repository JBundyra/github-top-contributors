# _GitHub Top Contributors_

The aim of this project is to provide a web service allowing a user to list top contributors for a given GitHub organization.

It exposes a single endpoint `GET /org/<GITHUB_ORG>/contributors` which then fetches the necessary data from GitHub API,
computes the result and returns it as a JSON array to the user.
The array contains contributors' logins and number of contributions sorted in the descending order.

## Requirements

The project is created with libraries:
* requests
* pandas
* flask

## Setup

To run this project:
```bash
python3 main.py
```

You can also, optionally, pass your personal GitHub token via `GITHUB_TOKEN` environment variable:
```bash
GITHUB_TOKEN='<your_token>' python3 main.py
```
GitHub token allows to increase GitHub's rate limit restriction. 

## Usage

When the server is running, you can try it out in another terminal window with the following command:
```bash
curl \
  -H "Accept: application/json" \
  http://localhost:8080/org/<GITHUB_ORG>/contributors
```

### Working example
```bash
curl \
  -H "Accept: application/json" \
  http://localhost:8080/org/EnterpriseQualityCoding/contributors
```




