import multiprocessing

from flask import Blueprint, jsonify, request
from weibospider.run import run_search, run_comment

spider_bp = Blueprint('spider', __name__, url_prefix='/spider')


@spider_bp.route('/search', methods=["POST"])
def search():
    try:
        keywords = request.json.get("keywords")
        start_date = request.json.get("start_date")
        end_date = request.json.get("end_date")
        process = multiprocessing.Process(target=run_search, args=(keywords, start_date, end_date))
        process.start()
        return jsonify(True)
    except Exception:
        return jsonify(False)
@spider_bp.route('/comment', methods=["POST"])
def comment():
    try:
        tweet_ids = request.json.get("tweet_ids")
        process = multiprocessing.Process(target=run_comment, args=tweet_ids)
        process.start()
        return jsonify(True)
    except Exception:
        return jsonify(False)
