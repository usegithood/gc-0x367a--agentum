def run(payload):
    """githood agent entrypoint. payload is the parsed request body."""
    return {"hello": "from githood", "echo": payload}
