import subprocess
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    """Receives Mizar code, runs the verifier, and returns the result."""
    code = request.json.get('code', '')
    
    # Securely create a temporary file to store the proof
    proof_filename = "temp_proof.miz"
    with open(proof_filename, 'w') as f:
        f.write(code)

    # Run the Mizar verifier command in a subprocess
    try:
        result = subprocess.run(
            ['mizf', proof_filename],
            capture_output=True,
            text=True,
            timeout=30  # Add a timeout for safety
        )
        
        # Combine standard output and standard error for a full report
        output = result.stdout + result.stderr
        
    except FileNotFoundError:
        output = "Error: 'mizf' command not found. Are you running this inside the Mizar Dev Container?"
    except Exception as e:
        output = f"An unexpected error occurred: {e}"
    finally:
        # Clean up the temporary file
        if os.path.exists(proof_filename):
            os.remove(proof_filename)

    return jsonify({'result': output})
