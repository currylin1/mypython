# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:37:50 2023

@author: 林奇叡
"""

from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

def ge_content(api_key, story):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": story}]}]}
    response = requests.post(url, headers=headers, json=data, params={'key': api_key})
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_story = ''
    if request.method == 'POST':
        story = request.form['story']
        api_key = '自行出入'
        response = ge_content(api_key, story)
        if response.status_code == 200:
            generated_story = format_response(response.json())
        else:
            generated_story = '無法獲得故事內容'
    return render_template('index_1.html', generated_story=generated_story)

def format_response(response):
    if response and 'candidates' in response and len(response['candidates']) > 0:
        content = response['candidates'][0]['content']
        parts = content.get('parts', [])
        story = ' '.join([part['text'] for part in parts])
        return story
    else:
        return "無法獲得故事內容"  

if __name__ == '__main__':
    app.run(debug=True)
