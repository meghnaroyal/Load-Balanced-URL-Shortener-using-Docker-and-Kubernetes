# app.py
from flask import Flask, request, jsonify, redirect
import redis
import hashlib
import os

app = Flask(__name__)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    long_url = data.get("long_url")
    if not long_url:
        return jsonify({"error": "Missing URL"}), 400
    short_id = hashlib.md5(long_url.encode()).hexdigest()[:6]
    redis_client.set(short_id, long_url)
    return jsonify({"short_url": f"http://localhost:5000/{short_id}"}), 200

@app.route("/<short_id>")
def redirect_to_url(short_id):
    long_url = redis_client.get(short_id)
    if long_url:
        return redirect(long_url, code=302)
    return jsonify({"error": "Short URL not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
