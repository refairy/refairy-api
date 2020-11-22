from flask import request

def check():
    data = request.get_json()
    response = {
        "origin": data["sentence"],
        "is_wrong": True,
        "category": "dokdo",
        "corredted": "Corrected sentence",
        "confidence": 0.8,
    }
    return response
