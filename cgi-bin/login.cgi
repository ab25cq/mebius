#!/usr/bin/python3

import cgi;
import cgitb;
import os;

user_data_dir = "data/"

cgitb.enable();

form = cgi.FieldStorage();

name = form["uid"].value;
password = form["pwd"].value;

invalid_password = False;

def check_password(name, password):
    with open(user_data_dir + name) as f:
        saved_password = f.read().chomp();
        
    if saved_password != password:
        invalid_password = True;

def create_user(name, password):
    with open(user_data_dir + name, mode='w') as f:
        f.write(password + "\n")

if os.path.exists(name):
    check_password(name, password);
else :
    create_user(name, password);


print("""
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>
Mebius
</title>
</head>
<body>
""");

if invalid_password:
    print("<p>パスワードがちがいます</p>");
else:
    print("<p>ログインできました。</p>");
    
print("</body></html>");

