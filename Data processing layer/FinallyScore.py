from flask import Flask, jsonify
import numpy as np
import AUR
import OverallScoring
import NodeScore
import time
import threading

app = Flask(__name__)

def calculate_final_score():
    a1 = AUR.certik_AUR_score()
    a2 = AUR.Chainsecurity_AUR_score
    a3 = AUR.experience_score
    a4 = AUR.defisafety_AUR_score
    b1 = OverallScoring.certik_score()
    b2 = OverallScoring.Chainsecurity_score()
    b3 = OverallScoring.Hacken_score()
    b4 = OverallScoring.defisafety_score()
    C = NodeScore.decentralization_score(7346,[0.2,0.2,0.2,0.1,0.1,0.1,0.1])
  
    final_score = 100 * {[(a1+b1)/2 + (a2+b2)/2 + (a3+b3)/2 + (a4+b4)/2] * 0.7 
    + (C * 0.3)}
    print(final_score)
    response = {
        'final_score': final_score
    }
    
    return response

def update_final_score():
    while True:
        final_score_response = calculate_final_score()
        app.config['FINAL_SCORE'] = final_score_response['final_score']
        print(f"Final score updated: {app.config['FINAL_SCORE']}")
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)

@app.route('/final_score', methods=['GET'])
def get_final_score():
    if 'FINAL_SCORE' not in app.config:
        final_score_response = calculate_final_score()
        app.config['FINAL_SCORE'] = final_score_response['final_score']
    
    return jsonify({'final_score': app.config['FINAL_SCORE']})

if __name__ == '__main__':
    update_thread = threading.Thread(target=update_final_score)
    update_thread.start()
    app.run(debug=True)


#http://192.168.10.246:5000/final_score