import requests
import json

def summarize_text(input_text):
    url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {hf_token}' # Replace with your actual token
    }

    payload = json.dumps({ "inputs": input_text })

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()

        result = response.json()
        
        if isinstance(result, list) and 'summary_text' in result[0]:
            return result[0]['summary_text']
        elif 'error' in result:
            return f"Error from API: {result['error']}"
        else:
            return "Unexpected response format from summarization API."

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

