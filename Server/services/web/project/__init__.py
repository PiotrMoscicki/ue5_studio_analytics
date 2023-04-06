import os

from flask import (
    Flask,
    jsonify,
    request,
    Response,
)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    ingest_time = db.Column(db.DateTime(), nullable=False)
    event = db.Column(db.JSON(), nullable=False)

    def __init__(self, ingest_time, event):
        self.ingest_time = ingest_time
        self.event = event


@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route("/datarouter/api/v1/public/data", methods=["POST"])
def studio_analytics_v1() -> Response:
    """Super simple implementation of the Epic public data endpoint."""
    args = request.args
    content = request.get_json()

    if content is not None:
        ingest_time = datetime.now(tz=timezone.utc)

        for event in content["Events"]:
            event.update(args)
            db.session.add(Event(ingest_time, event))
            db.session.commit()

    return Response("{}", status=201, mimetype="application/json")
