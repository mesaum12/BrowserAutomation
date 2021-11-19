import webbrowser as wb

def webautomation():
    urls=(
        "www.google.com",
        "www.github.com",
    )

    for url in urls:
        print("Opening :"+url)
        wb.get('firefox').open(url)

webautomation()