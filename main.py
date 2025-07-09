from parser import read_all_python_files
from summarizer import summarizer, user
import json
import os

# Optional: create output folder if not present
os.makedirs("output", exist_ok=True)

def summarize_all_code(input_folder, output_path):
    code_data = read_all_python_files(input_folder)
    all_summaries = []

    for file in code_data:
        filename = file["filename"]
        for element in file["elements"]:
            code_type = element["type"]
            name = element["name"]
            docstring = element["docstring"] or "No docstring provided"

            # 🧠 Construct the input prompt for AI
            prompt = f"""
Please summarize the following {code_type} from file `{filename}`:

Name: {name}
Docstring: {docstring}

Explain what this {code_type} does in simple terms.
"""

            print(f"\n🧠 Summarizing {code_type} `{name}` in {filename}...\n")

            # 🔁 Start AutoGen chat
            response = user.initiate_chat(summarizer, message=prompt)
            summary_text = response.summary.strip() if hasattr(response, "summary") else "No response"



            all_summaries.append({
                "file": filename,
                "type": code_type,
                "name": name,
                "prompt": prompt,
                "summary":summary_text
  # Optional – you can capture response if needed
            })

    # 💾 Save all prompts (can later enhance to include response)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_summaries, f, indent=2)

if __name__ == "__main__":
    summarize_all_code("input_code", "output/summary.json")


