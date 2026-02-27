import re
from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify
from agents.master_agent import process_farmer
from services.pdf_service import generate_pdf
from markdown import markdown

from flask import Flask, request, jsonify
from services.rag_service import RAGService
from services.llm_service import generate_response  # your existing LLM function

app = Flask(__name__)

# Initialize RAG
rag = RAGService()
rag.load_index()

app.secret_key = "supersecretkey"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    user_input = {
        "crop_type": request.form["crop_type"],
        "state": request.form["state"],
        "land_size": request.form["land_size"],
        "income_level": request.form["income_level"],
        "farming_type": request.form["farming_type"]
    }

    report = process_farmer(user_input)

    session["report"] = report
    session["user_input"] = user_input

    return redirect(url_for("result"))


@app.route("/generate_ajax", methods=["POST"])
def generate_ajax():
    """AJAX endpoint for generating report without page redirect"""
    user_input = {
        "crop_type": request.form.get("crop_type"),
        "state": request.form.get("state"),
        "land_size": request.form.get("land_size"),
        "income_level": request.form.get("income_level"),
        "farming_type": request.form.get("farming_type")
    }

    report = process_farmer(user_input)

    session["report"] = report
    session["user_input"] = user_input

    return jsonify({"success": True, "redirect_url": url_for("result")})


@app.route("/result")
def result():

    report_text = session.get("report")
    user_input = session.get("user_input", {})

    html_report = markdown(report_text)

    return render_template("result.html", report=html_report, user_input=user_input)


@app.route("/download")
def download():

    report_text = session.get("report")

    filename = generate_pdf(report_text)

    print("Generated filename:", filename)

    return send_file(
        filename,
        as_attachment=True,
        download_name="Agriculture_Report.pdf",
        mimetype="application/pdf"
    )


def clean_text(text):
    """
    Removes Markdown symbols like #, *, _, and formats the text for chatbot response.
    """
    text = re.sub(r'#+\s*', '', text)      # Remove headings (#, ##, ###)
    text = re.sub(r'\*\*|\*|__|_', '', text)  # Remove bold/italic
    text = re.sub(r'\n+', '\n', text)      # Collapse multiple newlines
    text = text.strip()                     # Remove extra spaces
    return text


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "Please enter a message."})

    # 1️⃣ Retrieve RAG chunks
    chunks = rag.retrieve(user_message, top_k=3)
    if not chunks:
        context = "No additional data found."
    else:
        context = "\n".join(chunks)

    # 2️⃣ Form prompt for LLM
    enhanced_prompt = f"""
    Use the following verified agricultural data:

    {context}

    Now answer the question:
    {user_message}
    """

    # 3️⃣ Get response from LLM
    raw_answer = generate_response(enhanced_prompt)

    # 4️⃣ Clean the answer
    clean_answer = clean_text(raw_answer)

    return jsonify({"response": clean_answer})


if __name__ == "__main__":
    app.run(debug=True)
