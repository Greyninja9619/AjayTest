from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()

        # Extract "System.Title" from the incoming webhook data
        title = data.get("resource", {}).get("fields", {}).get("System.Title", "")

        # Call the processing and posting function directly
        post_data_to_azure_devops(title)

        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

def process_webhook_data(data):
    # Your processing logic goes here
    # Modify as per your requirements
    processed_data = {"processed": True, "original_data": data}
    return processed_data

def post_data_to_azure_devops(data):
    # Your Azure DevOps REST API request logic goes here
    # Modify as per your requirements
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

    # Handle response (status code, etc.)
    if response.status_code != 200:
        raise Exception(f"Failed to post data to Azure DevOps. Status code: {response.status_code}, Response: {response.text}")

if __name__ == '__main__':
    app.run(debug=True)