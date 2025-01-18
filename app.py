from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoConfig, pipeline
from flask import Flask, render_template, request, jsonify

MODEL_NAME = "vinai/bartpho-syllable"
MAX_LENGTH = 512

model_folder = "saved_model"

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(model_folder, trust_remote_code=True)
corrector = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/correct',  methods=['POST'])
def correct_text():
    try:
        input_data = request.get_json()
        input_text = input_data.get("input_text", "")

        corrections = corrector(input_text, max_length=MAX_LENGTH, truncation=True)
        corrected_text = corrections[0]['generated_text']

        return jsonify({"corrected_text": corrected_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)