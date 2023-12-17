import re 
file = open('sampletext.txt')
text = file.read()
email_pat = r'[a-zA-Z0-9\.\+_]+@[a-zA-Z0-9\.\+]+.com'
mob_pat = r'[0-9]+[#\-*]*[0-9]+[0-9]+[#\-*]*[0-9]'
url_pat = "(https://|www.|http://)[a-zA-Z]+\.[a-zA-Z]+"
name_pat = r'M(?:r\.|rs\.|s\.) [a-zA-Z]+'

print(f"\nEmails in text field are : {re.findall(email_pat,text)}")
print(f"Phone numbers are : {re.findall(mob_pat,text)}")
print(f"Names are : {re.findall(name_pat,text)}")
print(f"Urls are : {[i.group() for i in re.finditer(url_pat,text)]}\n")