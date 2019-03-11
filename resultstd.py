#!f:/Python34/python.exe
import cgi
print("Content-Type: text/html")
print("""
""")

request=cgi.FieldStorage()

sn=request.getvalue('sn')

p=int(request.getvalue('p'))

c=int(request.getvalue('c'))
m=int(request.getvalue('m'))
t=p+c+m
p=t/3

res='';


if p>=60:
 res='Pass'
else:
 res='Fail'
 

print("<html>")
print("<b><i><font color='red'>{}</font></i></b>".format(sn));
print("<table border=1 cellspacing=5>");

print("<tr><th>Code</th><th>Name</th><th>Min</th><th>Max</th><th>Obtained</th></tr>");

print("<tr><td>100</td><td>Physics</td><td>60</td><td>100</td><td>{}</td></tr>".format(p))

print("<tr><td>200</td><td>Chemistry</td><td>60</td><td>100</td><td>{}</td></tr>".format(c))

print("<tr><td>300</td><td>Math</td><td>60</td><td>100</td><td>{}</td></tr>".format(m))

print("<tr><td>%age</td><td>{}</td><td>&nbsp;</td><td>Total</td><td>{}</td></tr>".format(p,t))

print("</table><br>")
print("Result:{}".format(res))
print("</html>");
