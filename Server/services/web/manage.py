from flask.cli import FlaskGroup

from project import app, db, Event
import requests
import click

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Event("2020-01-01", {"hello": "world"}))
    db.session.commit()

@cli.command("post_event")
@click.argument("event_file")
def post_event(event_file):
    with open(event_file, "r") as f:
        data = f.read()
    requests.post("http://localhost:5000/datarouter/api/v1/public/data", json=data)
    

@cli.command("get_events")
def get_events():
    events = Event.query.all()
    for event in events:
        print(event.id, event.ingest_time, event.event)

@cli.command("post_event_from_code")
def post_event_from_code():
    data = {
        "Events": [
            {
                "AppID": "SomethingUniqueToCompany",
                "UserID": "regnerblokandersen",
                "P4Branch": "++project+main",
                "FirstTime": True,
                "SessionID": "{40FD32AB-44A1-BD58-05E0-37A2A12E5300}",
                "AppVersion": "++project+main-CL-1111111",
                "DateOffset": "+00:00:52.108",
                "UploadType": "eteventstream",
                "LoadingName": "InitializeEditor",
                "ProjectName": "Project",
                "ComputerName": "Workstation",
                "AppEnvironment": "datacollector-binary",
                "LoadingSeconds": 112.776953
            }
        ]
    }
    requests.post("http://localhost:5000/datarouter/api/v1/public/data", json=data)

if __name__ == "__main__":
    cli()
