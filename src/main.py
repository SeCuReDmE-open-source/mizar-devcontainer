from server import app

if __name__ == '__main__':
    print("Starting Mizar Verification Server...")
    print("Access the UI at http://localhost:8080")
    # In GitHub Codespaces, the port will be forwarded automatically.
    app.run(host='0.0.0.0', port=8080)
