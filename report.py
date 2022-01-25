from __future__ import annotations
import typer
import questionary as qs
import json

custom_style = qs.Style([
	('qmark', 'fg:green'),
	('answer', 'fg:blue'),
	('pointer', 'fg:blue'),
	('highlighted', 'fg:blue')
	])

with open('choices.json') as f:
	choices: list[str] = json.load(f)

def main():
	title : str = qs.text("Name of the report:", style=custom_style).unsafe_ask()
	link : str = qs.text("Report link:", style=custom_style).unsafe_ask()
	preview_no = int(qs.text("No. of preview images:", style=custom_style).unsafe_ask())
	tag: str = qs.select("Type of the report:", choices=choices, pointer='❯', style=custom_style).unsafe_ask()

	if(tag == 'Something else'):
		tag = qs.text("New type").ask()
		choices.append(tag)
		with open('choices.json', 'w') as f:
			json.dump(choices, f)

	archive = qs.confirm("Is it archived report? ", style=custom_style).unsafe_ask()

	preview_link = f"https://tealindia-logos-static.s3.ap-south-1.amazonaws.com/research_reports/previews/{link}/01.png"
	previews = [preview_link.replace("01", str(x).zfill(2)) for x in range(1, preview_no + 1)]

	obj = {
		"title": title,
    "link": f"/research/{link}",
    "thumb": f"https://tealindia-logos-static.s3.ap-south-1.amazonaws.com/research_reports/previews/{link}/01.png",
    "previews": previews,
    "desc": "TEAL Analytics reports analyse quarterly  real estate activity including sale registrations, leasing activity, price trends, geographic trends and policy updates at a city and micro-market levels.",
    "report": f"https://tealindia-logos-static.s3.ap-south-1.amazonaws.com/research_reports/{link}.pdf",
    "type": tag,
    "archive": archive
	}
	print(json.dumps(obj, separators=(',', ':'), indent=2))


if __name__== "__main__":
	typer.run(main)