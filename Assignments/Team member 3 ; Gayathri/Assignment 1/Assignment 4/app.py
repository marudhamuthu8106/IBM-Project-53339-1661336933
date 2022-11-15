<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 7.4.2.3 (Windows)"/>
	<meta name="created" content="2022-11-15T15:20:41.863000000"/>
	<meta name="changed" content="2022-11-15T15:22:25.507000000"/>
</head>
<body lang="en-IN" dir="ltr"><p><br/>
<br/>

</p>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>from flask import Flask,
			render_template, request, url_for, flash, redirect</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>app = Flask(__name__)</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>app.config['SECRET_KEY']
			= 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>@app.route('/create/',
			methods=('GET', 'POST'))</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>def create():</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>if request.method ==
			'POST':</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>title =
			request.form['title']</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>content =
			request.form['content']</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>if not title:</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>flash('Title is
			required!')</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>elif not content:</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>flash('Content is
			required!')</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>else:</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>messages.append({'title':
			title, 'content': content})</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>name = &quot;Shyam Mohan&quot;</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>return
			redirect(url_for('index', messages=name ))</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>return
			render_template('create.html')</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>messages = [{'title':
			'Message One',</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>'content': 'Message One
			Content'},</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>{'title': 'Message Two',</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>'content': 'Message Two
			Content'}</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>]</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>@app.route('/')</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>def index():</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>return
			render_template('index.html', messages=messages)</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>@app.route('/admin')</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>def hello_admin():</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>return 'Hello Admin'</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>@app.route('/guest/&lt;guest&gt;')</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>def hello_guest(guest):</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>return 'Hello %s as
			Guest' % guest</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>@app.route('/user/&lt;name&gt;')</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>def hello_user(name):</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>if name =='admin':</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>return
			redirect(url_for('hello_admin'))</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>else:</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>return
			redirect(url_for('hello_guest',guest = name))</p>
		</td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"></td>
	</tr>
</table>
<table cellpadding="2" cellspacing="2">
	<tr>
		<td style="border: none; padding: 0cm"><p>if __name__ ==
			'__main__':</p>
		</td>
	</tr>
</table>
<p>app.run(host='0.0.0.0', port=5000, debug=True) 
</p>
</body>
</html>