from datetime import datetime, timedelta
from flask import Flask, jsonify, request

app = Flask(__name__)

class TimeManage:
    """A class to manage timers and keywords for emails."""

    def __init__(self):
        # Initialize dictionaries for timers and keywords
        self.timer = {
            'important': {},
            'external': {},
            'deals': {},
            'school': {},
            'free delivery': {},
            'available': {},
            'new': {},
            'alert': {},
            'news': {},
            'update': {},
            'summer': {},
            'weekend': {}
        }
        self.keywords = {}
        self.user_data = {}
        self.api_key = 'YOUR_API_KEY'
        self.api_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

    def set_timer(self, email, category, duration):
        """Set a timer for an email in a specified category."""
        if category not in self.timer:
            return "Category doesn't exist"
        
        target_time = datetime.now() + duration
        self.timer[category][email] = target_time
        return f"Timer set for {target_time}"

    def get_timer(self, email, category):
        """Get the timer for an email in a specified category."""
        if category in self.timer:
            return self.timer[category].get(email, "No timer set")
        return "Invalid category"

    def delete_timer(self, email, category):
        """Delete the timer for an email in a specified category."""
        if category in self.timer and email in self.timer[category]:
            del self.timer[category][email]
            return "Timer deleted"
        return "Timer not found"

    def del_keywords(self, category):
        """Delete keywords from the specified category."""
        if category in self.keywords:
            deleted_keywords = list(self.keywords[category].keys())
            del self.keywords[category]
            return deleted_keywords
        return "Category does not exist"

    def add_keywords(self, category, *words):
        """Add keywords to a specified category."""
        if category not in self.keywords:
            self.keywords[category] = {}
        for word in words:
            self.keywords[category][word] = True

# Define API endpoints
@app.route('/set_timer', methods=['POST'])
def api_set_timer():
    data = request.json
    email = data.get('email')
    category = data.get('category')
    duration = timedelta(minutes=data.get('duration', 0))  # Assuming duration is in minutes
    time_manager = TimeManage()
    result = time_manager.set_timer(email, category, duration)
    return jsonify({"message": result})
   
    if  duration_unit == 'minutes':
       duration=timedelta(minutes=duration_values)
    elif duration_unit =='hours':
        duration=timedelta(hours=duration_values)
    elif duration_unit =='days':
        duration=timedelta(days=duration_values)
    elif durtion_unit=='weeks':
     duration=timedelta(weeks=duration_values)
    elif duration_unit== 'months':
        duration=timedelta(days=30*duration_values)
    else:
        return jsonify({"Message: " "Invalid time frame"}),400 # 400 is error code to displ
    time_manager=TimeManage()
    result=time_manager.set_timer(email,category,duration)
    return jsonify({"message": result})
        

@app.route('/get_timer', methods=['GET'])
def api_get_timer():
    email = request.args.get('email')
    category = request.args.get('category')
    time_manager = TimeManage()
    timer_info = time_manager.get_timer(email, category)
    return jsonify({"timer_info": timer_info})

@app.route('/delete_timer', methods=['POST'])
def api_delete_timer():
    data = request.json
    email = data.get('email')
    category = data.get('category')
    time_manager = TimeManage()
    result = time_manager.delete_timer(email, category)
    return jsonify({"message": result})

@app.route('/del_keywords', methods=['POST'])
def api_del_keywords():
    data = request.json
    category = data.get('category')
    time_manager = TimeManage()
    deleted_keywords = time_manager.del_keywords(category)
    return jsonify({"deleted_keywords": deleted_keywords})

@app.route('/add_keywords', methods=['POST'])
def api_add_keywords():
    data = request.json
    category = data.get('category')
    words = data.get('words', [])
    time_manager = TimeManage()
    time_manager.add_keywords(category, *words)
    return jsonify({"message": "Keywords added successfully"})

if __name__ == '__main__':
    app.run(debug=True)
