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

        # Extract "System.Title" from the incoming webhook data   System.TeamProject
        title = data.get("resource", {}).get("fields", {}).get("System.Title", "")
        description = data.get("resource", {}).get("fields", {}).get("System.Description", "")
        TeamProject = data.get("resource", {}).get("fields", {}).get("System.TeamProject", "")
        url = f"https://dev.azure.com/itsmeuzair/{TeamProject}/_apis/wit/workitems/$Issue?api-version=7.1-preview.3"
        
        personal_access_token = "oihemdcq2y2hluor2zp357h7a6rt7q3pr45hb3xycwlrkztl5s2a"
        
        body = [
         {
         "op": "add",
         "path": "/fields/System.Title",
         "value": title
         },
         {
         "op": "add",
         "path": "/fields/System.Description",
         "value": description
         }   
        ]
        
        response = requests.post(url, json=body, headers={'Content-Type': 'application/json-patch+json'}, auth=('', personal_access_token))
        
        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500
