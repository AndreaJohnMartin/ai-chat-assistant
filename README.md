# 🤖 Martia: Your Personal AI Assistant

Martia is a simple yet powerful AI chat assistant built with Flask and OpenRouter's GPT API. It allows users to ask questions and receive intelligent responses, all from a clean, minimal web interface.

![Martia UI](https://github.com/user-attachments/assets/732ad1f9-a471-455c-8461-02f785733646)

---

## 🌟 Features

- Ask anything – factual or fun
- Real-time chat interface
- Integration with GPT-3.5 via OpenRouter
- Secure API key handling with `.env` file
- Lightweight Flask backend

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- `pip` installed

### 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/AndreaJohnMartin/ai-chat-assistant.git
   cd ai-chat-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment**
   Create a `.env` file in the root directory and add:
   ```env
   API_KEY=sk-xxxxx-your-openrouter-key
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Example Prompts

- "Tell me a fun fact"
- "What is Artificial Intelligence?"
- "Summarize the story of Mahabharata"
- "Generate a haiku about space"

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **API**: OpenRouter (uses GPT-3.5 model)

---

## 🔐 Environment Variables

Make sure your `.env` file is **not** committed to GitHub.  
It should contain your OpenRouter API key:

```env
API_KEY=your-openrouter-api-key
```

---

## 📸 Screenshots

![Chat Input](https://github.com/user-attachments/assets/259eaae3-2127-4f26-af37-e76efbc9d2a3)  
![Chat Response](https://github.com/user-attachments/assets/836bab03-b934-49a5-9d6c-a3badb80eff8)  
![More Examples](https://github.com/user-attachments/assets/1bfb6e78-61f6-41fd-ac69-076ab555b13a)  
![Summary Example](https://github.com/user-attachments/assets/f3f37e8d-02ba-4f80-b361-6798193247c6)  
![Main Page](https://github.com/user-attachments/assets/0d0eeece-f430-4029-94a7-10fc280fbab4)  
![Prompt History](https://github.com/user-attachments/assets/7126aa86-56bd-4339-8c50-129702a695b6)

---

## 📚 Acknowledgements

- OpenAI / OpenRouter for API access  
- Flask for the lightweight backend framework

---

## 👨‍💻 Author

Developed by **Andrea John Martin**  
For **Vault of Codes – AI & Prompt Engineering Internship (Final Project)**

---

## 📎 License

This project is open-source and free to use under the [MIT License](LICENSE).
