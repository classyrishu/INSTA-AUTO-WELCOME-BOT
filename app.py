import os, time, threading
from flask import Flask
from instagrapi import Client

app = Flask(__name__)

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
GROUP_NAMES = os.getenv("GROUP_NAMES", "Cloud Berry 🍓|🌙 𓆩MOONLIGHT𓆪 ✨").split("|")
WELCOME_MSG = os.getenv("WELCOME_MSG", "HELLO JAANU WELCOME TO OUR GC TOH KESE HO AAP , INTRO BHI DE BC")

seen = {}

def bot_loop():
    cl = Client()
    try:
        cl.login(USERNAME, PASSWORD)
        print("Login ho gaya")
    except Exception as e:
        print("Login fail:", e)
        return
    while True:
        try:
            threads = cl.direct_threads(amount=20)
            for t in threads:
                title = (t.thread_title or "").strip()
                if title in [g.strip() for g in GROUP_NAMES]:
                    if t.id not in seen:
                        seen[t.id] = set([u.pk for u in t.users])
                        continue
                    current = set([u.pk for u in t.users])
                    new_ones = current - seen[t.id]
                    for nid in new_ones:
                        cl.direct_send(WELCOME_MSG, thread_ids=[t.id])
                        print(f"Welcome bheja {title} me")
                        seen[t.id].add(nid)
            time.sleep(30)
        except Exception as e:
            print("Error:", e)
            time.sleep(60)

threading.Thread(target=bot_loop, daemon=True).start()

@app.route('/')
def home():
    return "IG GC Welcome Bot is Running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
