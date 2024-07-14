import webbrowser

def generate_link():
    # Your code to generate the link
    link = "https://google.com"  # Replace this with your actual link generation logic
    return link

def open_link_in_browser(link):
    webbrowser.open(link)

if __name__ == "__main__":
    link = generate_link()
    open_link_in_browser(link)
