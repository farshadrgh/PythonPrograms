import requests

#https://www.breakingnewsenglish.com/ for example
res = requests.get('https://www.breakingnewsenglish.com/')
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("Response text of https://breakingnewsenglish.com/:")
print(res.text)
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print("Content of the said url:")
print(res.content)
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print("Raw data of the said url:")
r = requests.get('https://api.github.com/events', stream = True)
print(r.raw)
print(r.raw.read(20))
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")