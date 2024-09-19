from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # List of your links with names, URLs, and icons
    links = [
        {"name": "Website", "url": "https://cybergeneration.tech", "icon": "fas fa-globe"},
        {"name": "Discord", "url": "https://discord.gg/QM7mgqB3BD", "icon": "fab fa-discord"},
        {"name": "YouTube", "url": "https://youtube.com/@cybergenenation?si=SJr70X8anm8A9CTh", "icon": "fab fa-youtube"},
        {"name": "GitHub", "url": "https://github.com/Cybargeneration", "icon": "fab fa-github"},
    ]
    return render_template('index.html', links=links)

# Contact Me route
@app.route('/contact')
def contact():
    return redirect('https://cybergeneration.tech/contact')  # Replace with your contact page URL

if __name__ == '__main__':
    app.run(debug=True)

