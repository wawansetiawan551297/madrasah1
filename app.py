from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
import sqlite3, json

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "database_absensi_mi_miftahul_athfal.db"
app = Flask(__name__, static_folder=None)
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS app_state (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                state_json TEXT NOT NULL,
                updated_at TEXT NOT NULL DEFAULT (datetime('now','localtime'))
            )
        """)

@app.get("/")
def index():
    return send_from_directory(ROOT, "index.html")

@app.get("/api/state")
def get_state():
    with connect() as conn:
        row = conn.execute("SELECT state_json FROM app_state WHERE id=1").fetchone()
    return jsonify({"state": json.loads(row["state_json"]) if row else None})

@app.post("/api/state")
def save_state():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict) or not isinstance(payload.get("state"), dict):
        return jsonify({"error": "Format data tidak valid"}), 400
    state = payload["state"]
    # Basic shape validation so unrelated payloads are not saved accidentally.
    if not isinstance(state.get("people", {}), dict) or not isinstance(state.get("logs", []), list):
        return jsonify({"error": "Struktur data absensi tidak valid"}), 400
    encoded = json.dumps(state, ensure_ascii=False, separators=(",", ":"))
    with connect() as conn:
        conn.execute("""
            INSERT INTO app_state (id, state_json, updated_at)
            VALUES (1, ?, datetime('now','localtime'))
            ON CONFLICT(id) DO UPDATE SET
              state_json=excluded.state_json,
              updated_at=excluded.updated_at
        """, (encoded,))
    return jsonify({"ok": True})

@app.get("/api/health")
def health():
    return jsonify({"ok": True, "database": DB_PATH.name})

if __name__ == "__main__":
    init_db()
    print("Absensi RFID berjalan di http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)
