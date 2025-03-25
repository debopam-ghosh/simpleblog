import os
os.makedirs('templates', exist_ok=True)

home_html = """<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Blog</h1>
    {% for post in posts %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
        <small>By {{ post.author }}</small>
    {% endfor %}
    <a href="{{ url_for('post') }}">Create Post</a> |
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>"""

register_html = """<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username }}<br>
        {{ form.email.label }} {{ form.email }}<br>
        {{ form.password.label }} {{ form.password }}<br>
        {{ form.confirm_password.label }} {{ form.confirm_password }}<br>
        {{ form.submit }}
    </form>
</body>
</html>"""

login_html = """<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.email.label }} {{ form.email }}<br>
        {{ form.password.label }} {{ form.password }}<br>
        {{ form.submit }}
    </form>
</body>
</html>"""

post_html = """<!DOCTYPE html>
<html>
<head>
    <title>Create Post</title>
</head>
<body>
    <h1>Create a New Post</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.title.label }} {{ form.title }}<br>
        {{ form.content.label }} {{ form.content }}<br>
        {{ form.submit }}
    </form>
</body>
</html>"""

with open('templates/home.html', 'w') as f:
    f.write(home_html)
with open('templates/register.html', 'w') as f:
    f.write(register_html)
with open('templates/login.html', 'w') as f:
    f.write(login_html)
with open('templates/post.html', 'w') as f:
    f.write(post_html)
