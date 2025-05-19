import click
from bs4 import BeautifulSoup
from transformers import pipeline
import urllib.request


def extract_from_url(url):
    text = ""
    req = urllib.request.Request(
        url, data=None,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }
    )
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    for paragraph in soup.find_all('p'):
        print(paragraph.text)
        text += paragraph.text

    return text


def process(text):
    summarizer = pipeline('summarization', model='t5-small')
    summary=summarizer(text,max_length=180)
    click.echo('Summarization processed successfully!')
    click.echo('='*8)
    return summary[0]['summary_text']

@click.command()
@click.option('--url')
@click.option('--file')
def main(url , file):
    if url:
        text = extract_from_url(url)
    elif file:
        with open(file ,'r') as _f:
            text = _f.read()
    click.echo(f'Summarization text from {url or file}')
    click.echo(process(text))


