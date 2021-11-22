import ccxt
import gunicorn
import json, config
from flask import Flask, request, jsonify, render_template



def mate(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    exchange = ccxt.config.EXCHANGE({
    "apiKey": config.API_KEY,
    "secret": config.SECRET_KEY
    })
    

    data = request.get_json()
    if 'token' not in data or data['token'] != config.TRADINGVIEW_TOKEN:
        return {
          "code" : "ERROR"
          "message" : "Hey mate! Is it you ringing the bell?"
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return 
