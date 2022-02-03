import urllib.request

url1 = "https://images.unsplash.com/photo-1505678261036-a3fcc5e884ee?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"

urlliste= [url1]
say = 1

for url in urlliste:
    urllib.request.urlretrieve(url, "resim" + str(say) + ".jpg")
    say +=1