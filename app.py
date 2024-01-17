from flask import Flask, request, jsonify
import base64
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hi Uzair</h1>"
    
@app.route("/about")
def uzair():
    return "<h1>About page</h1>"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()

        # Extract "System.Title" from the incoming webhook data
        title = data.get("resource", {}).get("fields", {}).get("System.Title", "")
        azure_devops_api_url = "https://dev.azure.com/itsmeuzair/TestProject/_apis/wit/workitems/Bug?api-version=7.1-preview.3"
        personal_access_token = "oihemdcq2y2hluor2zp357h7a6rt7q3pr45hb3xycwlrkztl5s2a"
        Token = base64.b64encode(bytes(':' + personal_access_token, 'utf-8')).decode('utf-8')
        headers = {
            'Authorization': 'Basic ' + Token,
            'Content-Type': 'application/json'
        }
        body = {
            "op": "add",
            "path": "/fields/System.Title",
            "from": None,
            "value": title
        }
        response = requests.post(azure_devops_api_url, json=body, headers=headers)
        
        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500
