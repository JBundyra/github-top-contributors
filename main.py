from flask import Flask, jsonify
from contributors_service import get_contributions_for_organization
import os

app = Flask(__name__)

github_token = os.getenv('GITHUB_TOKEN')


@app.route("/org/<org_name>/contributors", methods=['GET'])
def index(org_name):
    contributions = get_contributions_for_organization(org_name, github_token)
    return jsonify(contributions)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
