questions = [
    {
        'question': "What is the capital of France?",
        'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'answer': 3
    },
    {
        'question': "What is the largest planet in our Solar System?",
        'options': ['Earth', 'Jupiter', 'Mars', 'Venus'],
        'answer': 2
    },
    {
        'question': "What is the chemical symbol for water?",
        'options': ['O2', 'H2O', 'CO2', 'HO2'],
        'answer': 2
    },
    {
        'question': "Which country is known as the Land of the Rising Sun?",
        'options': ['China', 'Japan', 'South Korea', 'Thailand'],
        'answer': 2
    },
    {
        'question': "How many continents are there on Earth?",
        'options': ['5', '6', '7', '8'],
        'answer': 3
    }
]

async def ask_question(update, context):
    question_index = context.user_data['current_question']
    question = questions[question_index]
    options_text = "\n".join([f"{i + 1}. {option}" for i, option in enumerate(question['options'])])
    await update.message.reply_text(f"{question['question']}\n\n{options_text}")
