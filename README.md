

### 📄 YouTube Summarizer using GenAI (OpenAI)

YouTube Summarizer is a Python-based CLI tool that automatically fetches YouTube video transcripts and generates concise summaries using OpenAI’s GPT-3.5 Turbo model. Ideal for students, researchers, or anyone wanting to consume long video content quickly.

⸻

#### ✨ Features <br>
	•	🎯 Automatic Transcript Extraction – Uses youtube-transcript-api to fetch English subtitles from public YouTube videos.
	•	🧠 Smart Summarization – Uses OpenAI’s ChatCompletion API to generate clean, concise summaries.
	•	🛡️ Error Handling – Gracefully handles missing or disabled transcripts.
	•	🔐 Secure API Access – API key is managed through .env file for safety and reusability.
	•	🖥️ Command-line Interface (CLI) – Lightweight, fast, and easy to use from your terminal.

⸻

#### 🛠 Tech Stack<br>
	•	Python
	•	OpenAI API
	•	YouTube Transcript API
	•	python-dotenv

⸻

#### 🚀 How It Works<br>
	1.	Paste a YouTube video URL into the command line.
	2.	The tool extracts the video ID and fetches available English transcript.
	3.	The transcript is sent to OpenAI’s GPT-3.5 Turbo model
	4.	The tool prints a clean summary of the video content.

⸻

#### 🧩 Installation<br>

1. Clone the Repository<br>

git clone https://github.com/shavilya/YouTube-Summarizer-GenAI-openai.git
cd YouTube-Summarizer-GenAI-openai<br>

2. Install Dependencies<br>

pip install -r requirements.txt<br>

3. Set Up .env File<br>

Create a .env file in the root directory and add your OpenAI API key:<br>

OPENAI_API_KEY=your_openai_key_here<br>


⸻

#### ▶️ Usage <br>

python youtube_summarizer_using_openai.py<br>

📥 Paste the YouTube video URL when prompted.<br>
📃 If a transcript is available, it will be summarized and printed.<br>

⸻

#### 🧪 Example Output<br>

Enter YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ<br>

Transcript fetched successfully. Summarizing...<br>

Summary: The video discusses the emotional and cultural relevance of 80s pop music, focusing on themes of love, nostalgia, and digital transformation.<br>


⸻

#### 📌 Notes <br>
	•	Works only with videos that have English subtitles enabled.
	•	Summaries are concise (~150 tokens) and optimized for quick reading.
	•	You can customize the summary length by adjusting the max_tokens parameter.

⸻

#### 📬 Future Improvements <br>
	•	Convert to a web-based Streamlit app
	•	Add support for multiple languages
	•	Export summary to .txt or .pdf
	•	Option to summarize playlists



