from pathlib import Path
import json

intends_path = Path(__file__).with_name("intends.json")
querys_path = Path(__file__).with_name("querys.json")
responses_path = Path(__file__).with_name("responses.json")
related_path = Path(__file__).with_name("related.json")

intends = json.load(open(intends_path))
querys = json.load(open(querys_path))
responses = json.load(open(responses_path))
related = json.load(open(related_path))