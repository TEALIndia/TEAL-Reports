from __future__ import annotations
import typer
import questionary as qs
import json
import os
import fitz

custom_style = qs.Style([
    ('qmark', 'fg:green'),
    ('answer', 'fg:blue'),
    ('pointer', 'fg:blue'),
    ('highlighted', 'fg:blue')
])

with open("choices.json") as f:
  choices: list[str] = json.load(f)


def main():
  title: str = qs.text("Name of the report:", style=custom_style).unsafe_ask()
  link: str = qs.text("Report link:", style=custom_style).unsafe_ask()
  tag: str = qs.select(
      "Type of the report:", choices=choices, pointer="❯", style=custom_style
  ).unsafe_ask()
  archive = qs.confirm("Is it archived report? ", style=custom_style).unsafe_ask()

  os.mkdir(link)
  # To get better resolution
  zoom_x = 2.0  # horizontal zoom
  zoom_y = 2.0  # vertical zoom
  mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

  doc = fitz.open(link + '.pdf')  # open document
  for page in doc:  # iterate through the pages
    pix = page.get_pixmap(matrix=mat)  # render page to an image
    pix.save(f"{link}/{str(page.number + 1).zfill(2)}.png")  # store image as a PNG

  if tag == "Something else":
    tag = qs.text("New type").ask()
    choices.append(tag)
    with open("choices.json", "w") as f:
      json.dump(choices, f)

  obj = {
      "title": title,
      "link": link,
      "preview_no": len(doc),
      "desc": "TEAL Analytics reports analyse quarterly  real estate activity including sale registrations, leasing activity, price trends, geographic trends and policy updates at a city and micro-market levels.",
      "type": tag,
      "archive": archive,
  }
  print(json.dumps(obj, separators=(",", ":"), indent=2))


if __name__ == "__main__":
  typer.run(main)
