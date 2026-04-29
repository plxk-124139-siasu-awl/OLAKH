# ओळख Olakh — Build Your Business Identity Online 🇮🇳

> AI-powered website builder for local Indian businesses. Get online in 3 minutes, in your language, for free.

---

## What is Olakh?

63 million local businesses in India have no online presence — not because they don't want one, but because every existing solution is too expensive, too complicated, or not in their language.

Olakh fixes that. Fill a simple form, get a real website in seconds.

---

## Features

- 🤖 **AI Website Generation** — Powered by Groq API (Llama 3.3 70B)
- 🗣️ **10 Indian Languages** — Hindi, Punjabi, Marathi, Tamil, Telugu, Bengali, Gujarati, Kannada, Odia, Urdu
- 💬 **WhatsApp Integration** — Auto-added to every generated website
- 📱 **Phone Mockup Preview** — See your website in a real mobile preview instantly
- 🧑‍💼 **Business Dashboard** — Manage websites, view stats, track plan
- 💰 **Freemium Model** — Free to start, upgrade when ready
- 🔐 **Login & Signup** — Email based authentication with captcha

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python + Flask |
| AI Engine | Groq API — Llama 3.3 70B |
| Frontend | HTML, CSS, JavaScript |
| Environment | python-dotenv |

---

## Project Structure

```
olakh/
│
├── app.py              # Flask backend + Groq API integration
├── .env.example        # Template for environment variables
└── templates/
    └── index.html      # Frontend — landing page, dashboard, generator
```

---

## How It Works

1. User lands on Olakh and reads what it offers
2. Clicks **"Proceed to Create Your Website"**
3. **Signs up** with email — verifies with OTP — sets password
4. **Logs in** with email, password and captcha verification
5. Lands on their personal **dashboard**
6. Fills the website creation form — business name, type, location, phone, language
7. Flask sends a structured prompt to **Groq API**
8. **Llama 3.3 70B** generates a complete HTML website in their chosen language
9. Website renders instantly inside a **phone mockup preview**
10. Business owner shares their link or upgrades for more features

---

## Supported Languages

Hindi • Punjabi • Marathi • Tamil • Telugu • Bengali • Gujarati • Kannada • Odia • Urdu • English

---

## Pricing Model

| Plan | Price | Features |
|---|---|---|
| Free | ₹0/month | 1 website, Olakh subdomain, WhatsApp button |
| Pro | ₹199/month | Custom domain, Google listing, Analytics |
| Pro Plus | ₹399/month | Booking system, Online complete management, Custom workflow |

---

## Environment Variables

Copy `.env.example` to `.env` and fill in your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

> Get your free Groq API key at [console.groq.com](https://console.groq.com)

---

🔗 **Live Demo:** [olakh.onrender.com](https://olakh.onrender.com)
---

## Built By

Made with passion in India 🇮🇳

Building digital identity for every local business that deserves to be found online.

---

## License

MIT License — free to use, modify, and distribute.
