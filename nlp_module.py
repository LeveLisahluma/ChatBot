import spacy
from question_utility import ask_question, questions

nlp = spacy.load("en_core_web_sm")

async def handle_answer(update, context):
    user_input = update.message.text.strip()
    doc = nlp(user_input)

    question_index = context.user_data['current_question']
    correct_answer_index = questions[question_index]['answer']
    correct_answer_text = questions[question_index]['options'][correct_answer_index - 1].lower()

    user_answer = None

    # Check if input is numeric
    if any(token.like_num for token in doc):
        try:
            user_answer = int(user_input)
        except ValueError:
            pass

    # Check if input matches option text
    if user_answer is None:
        cleaned_input = user_input.lower()
        for i, option in enumerate(questions[question_index]['options'], start=1):
            if cleaned_input in option.lower():
                user_answer = i
                break

        # Optional: check named entities
        if user_answer is None:
            entities = [ent.text.lower() for ent in doc.ents]
            for i, option in enumerate(questions[question_index]['options'], start=1):
                if option.lower() in entities:
                    user_answer = i
                    break

    # Evaluate
    if user_answer == correct_answer_index:
        context.user_data['score'] += 1
        await update.message.reply_text("✅ Correct!")
    else:
        await update.message.reply_text(f"❌ Incorrect. The correct answer was: {correct_answer_text.title()}.")

    # Move to next question or finish
    context.user_data['current_question'] += 1
    if context.user_data['current_question'] < len(questions):
        await ask_question(update, context)
    else:
        score = context.user_data['score']
        await update.message.reply_text(f"🎉 Quiz finished! Your score is {score}/{len(questions)}.")
