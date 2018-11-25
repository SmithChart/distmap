# distmap

Welcome to the distmap backend repository.

Distmap is a tool to visualize travel time from one location
to a whole area using a heatmap.

Distmap was created by the distmap working group during the
"Smart City Braunschweig" Hackathon 2018.

## What you need

This project consists of three parts:

* backend (this repo)
* frontend
* documentation


## How to run the backend

You need to have an osm map next to your main.py:

```bash
wget https://overpass-api.de/api/map?bbox=10.4320,52.2083,10.6717,52.3066 -O map
```

Afterwards you can install the python3-dependencies and run the server:

```bash
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements-backend.txt
./main.py 
```
