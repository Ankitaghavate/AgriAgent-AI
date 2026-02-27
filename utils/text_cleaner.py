import markdown
from bs4 import BeautifulSoup


def markdown_to_clean_text(md_text):
    # Convert markdown to HTML
    html = markdown.markdown(md_text)

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # Extract clean text
    clean_text = soup.get_text("\n")

    return clean_text
