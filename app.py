from flask import Flask, abort, request
from flask_cors import CORS
import whisper
from tempfile import NamedTemporaryFile

# Load the Whisper model:
model = whisper.load_model('small')

app = Flask(__name__)
CORS(app)

@app.route('/text', methods=['POST'])
def handler():
    if not request.files:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400)

    # For each file, let's store the results in a list of dictionaries.
    results = []

    # Loop over every file that the user submitted.
    for filename, handle in request.files.items():
        # Create a temporary file.
        # The location of the temporary file is available in `temp.name`.
        temp = NamedTemporaryFile()
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(temp)
        # Let's get the transcript of the temporary file.
        result = model.transcribe(temp.name)
        # Now we can store the result object for this file.
        results.append({
            'filename': filename,
            'transcript': result['text'],
        })

    # This will be automatically converted to JSON.
    return {'results': results}

# transcrip the audio file and return the text

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if not request.files:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400)
     
    # For each file, let's store the results in a list of dictionaries.
    results = []
    # Loop over every file that the user submitted.
    for filename, handle in request.files.items():
        # Create a temporary file.
        # The location of the temporary file is available in `temp.name`.
        temp = NamedTemporaryFile()
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(temp)
        # traduce el audio a texto a Ingles
        result = model.transcribe(audio=temp.name,  task='translate', language='fr')
        # Now we can store the result object for this file.
        results.append({
            'filename': filename,
            'transcript': result['text'],
        })

    # This will be automatically converted to JSON.
    return {'results': results}
    
@app.route('/transcribe/<lang>', methods=['POST'])
def transcribe_fr(lang):
    if not request.files:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400)
     
    # For each file, let's store the results in a list of dictionaries.
    results = []
    # Loop over every file that the user submitted.
    for filename, handle in request.files.items():
        # Create a temporary file.
        # The location of the temporary file is available in `temp.name`.
        temp = NamedTemporaryFile()
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(temp)
        # traduce el audio a texto a Ingles
        result = model.transcribe(temp.name, language = lang)
        # Now we can store the result object for this file.
        results.append({
            'filename': filename,
            'transcript': result['text'],
        })

    # This will be automatically converted to JSON.
    return {'results': results}