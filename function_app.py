import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()
@app.function_name('ReadHTTPFunction')
@app.route(route="newroute2")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request in ReadHTTPFunction')

    try:
        # Parse JSON from the request body
        data = req.get_json()
    except ValueError as e:
        error_message = f"Error parsing JSON: {str(e)}"
        logging.error(error_message)
        return func.HttpResponse(error_message, status_code=400)

    # Initialize a list to hold all transcripts
    all_transcripts = []

    # Check if 'videos' key exists and iterate over each video
    if 'videos' in data:
        for video in data['videos']:
            # Check if 'insights' and 'transcript' keys exist for the video
            if 'insights' in video and 'transcript' in video['insights']:
                # Iterate over each transcript item and add it to the list
                for transcript_item in video['insights']['transcript']:
                    all_transcripts.append(transcript_item)

    # Convert the list of all transcripts to JSON string for the response
    response_content = json.dumps(all_transcripts)

    return func.HttpResponse(response_content, status_code=200, mimetype="application/json")
