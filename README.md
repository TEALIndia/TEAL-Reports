# TEAL - Research Reports

## Installation

1. Install latest version of python version 3 from the [official site](www.python.org) for your OS.
2. Install `questionary` and `pymupdf` python modules with

```sh
$ pip install questionary pymupdf fitz
```

## Get thumbnails & catalogue

1. Rename the pdf with link that would be shown in the website. A general rule f thumb is to convert the name of the report to lowercase and replace `spaces(" ")` with `dash("-")`.
2. Run report.py with

**Windows**

```sh
python report.py
```

**Linux/MacOS**

```sh
python3 report.py
```

3. This interactive cli will ask for report name, link (paste the same one you created in the first step), type and if it is to be archived or not. Provide relevant information.
4. In your terminal you would get json data printed as well you would get all the thumbnails of the pdf in the respective folder.
5. Copy the json data from your terminal.
6. Find the first item of your document type (Sales & Lease, Mortgage etc.) in `catalogue_new.json`.
7. Paste the copied data before that.

## Upload to s3 bucket

1. Go to [research_reports](https://s3.console.aws.amazon.com/s3/buckets/tealindia-logos-static?prefix=research_reports/&region=ap-south-1) s3 bucket.
2. If you don't have access or account in s3 then ask [Shreyas](https://github.com/wireman27) or someone else to give access credentials to the `research_reports` s3 bucket.
3. Create a folder with link (that you created earlier) as folder name.
4. Upload first 3 thumbnails in that folder, give read permission to everyone and save the changes.
5. Now go back to `research_report` folder.
6. Upload your report pdf and the newly updated `catalogue.json`.

And your report is live on [TEAL website](https://tealindia.in/research) !
