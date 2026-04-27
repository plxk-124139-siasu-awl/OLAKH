from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
import os
print("DEBUG:", os.getenv("GROQ_API_KEY"))
app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
@app.route("/generate", methods=["POST"])
def generate():
    business_name = request.form.get("business_name")
    business_type = request.form.get("business_type")
    location = request.form.get("location")
    phone = request.form.get("phone")
    description = request.form.get("description")
    language = request.form.get("language")

    prompt = f"""
    Create a complete, beautiful single-page HTML website for a local Indian business.
    
    Business Details:
    - Name: {business_name}
    - Type: {business_type}
    - Location: {location}
    - Phone: {phone}
    - Description: {description}
    
    VERY IMPORTANT - Language Instructions:
    - You MUST write ALL website content ONLY in {language}
    - If language is English: write everything in English only
    - If language is Hindi: write everything in Hindi using Devanagari script
    - If language is Punjabi: write everything in Punjabi using Gurmukhi script
    - If language is Marathi: write everything in Marathi using Devanagari script
    - If language is Tamil: write everything in Tamil script only
    - If language is Telugu: write everything in Telugu script only
    - If language is Bengali: write everything in Bengali script only
    - If language is Gujarati: write everything in Gujarati script only
    - If language is Kannada: write everything in Kannada script only
    - If language is Odia: write everything in Odia script only
    - If language is Urdu: write everything in Urdu script only
    - Keep business name, phone number and address as-is
    - Do NOT mix languages — use {language} only throughout
    
    Website Requirements:
    - Write ONLY the HTML code, nothing else, no explanation
    - Make it mobile friendly
    - Include a header with business name
    - Include an about section
    - Include services/products section
    - Include contact section with phone and location
    - Use warm Indian colors (saffron, green, white)
    - Make it look professional and trustworthy
    - Add a WhatsApp button linking to wa.me/{phone}
    - Do NOT include any explanation, only pure HTML code
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=3000,
    )

    generated_website = response.choices[0].message.content
    
    generated_website = generated_website.replace("```html", "").replace("```", "").strip()

    import json
    return f"""
    <script>
        window.opener = window.opener || window.parent;
        localStorage.setItem('olakh_generated_html', {json.dumps(generated_website)});
        localStorage.setItem('olakh_business_name', {json.dumps(business_name)});
        window.location.href = '/?generated=true';
    </script>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
