import json

def public_func():
    internal(1)
    internal(2)

def internal(n):
    json.dumps({'number': n})
