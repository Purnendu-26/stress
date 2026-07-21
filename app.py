from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

zone_explanations = {
    'Low': "You're experiencing low stress levels. Keep up your healthy habits!",
    'Moderate': "You're feeling moderate stress. It's a good time to implement some stress management techniques.",
    'High': "Your stress levels are high. Consider taking steps to reduce stress and prioritize self-care."
}

wellness_recommendations = {
    'Low': [
        "Maintain your current healthy sleep schedule (7-9 hours nightly",
        "Continue regular physical activity",
        "Practice mindfulness meditation a few times per week",
        "Stay connected with friends and family"
    ],
    'Moderate': [
        "Try 10 minutes of deep breathing exercises daily",
        "Take short breaks during work/study",
        "Prioritize 7-8 hours of sleep",
        "Incorporate light exercise like walking",
        "Limit caffeine and alcohol intake"
    ],
    'High': [
        "Practice relaxation techniques (progressive muscle relaxation)",
        "Consider journal your thoughts and feelings",
        "Aim for 8 hours of sleep consistently",
        "Engage in gentle yoga or stretching",
        "Talk to a trusted friend or counselor",
        "Take a digital detox for 30 minutes daily"
    ]
}

daily_habits = [
    "Start your day with a glass of water",
    "Take 5-minute stretch breaks every hour",
    "Eat at least one nutritious meal",
    "Step outside for fresh air",
    "Express gratitude for three things daily"
]

def get_stress_zone(total_score):
    if total_score <= 13:
        return 'Low'
    elif total_score <= 26:
        return 'Moderate'
    else:
        return 'High'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        answers = [int(data[f'q{i}']) for i in range(1, 11)]
        total_score = sum(answers)
        stress_zone = get_stress_zone(total_score)
        
        return jsonify({
            'score': total_score,
            'zone': stress_zone,
            'explanation': zone_explanations[stress_zone],
            'recommendations': wellness_recommendations[stress_zone],
            'daily_habits': daily_habits
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
