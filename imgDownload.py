
import urllib.request

# Base URL for the images
baseUrl = "https://studio.code.org/v3/assets/ms9D5GpZxzPEfovLBJIxxpC_8lGB5T-pF8rX8dM5QOE/"

# List of images to download
dic = [
    "P.gif",
    "R.gif",
    "S.gif",
    "P2.gif",
    "R2.gif",
    "S2.gif",
    "You-Default-IMage.png",
    "Bot-Default-IMage.png",
    "paper.png",
    "rock.png",
    "scissors.png",
]

# Download the images
for i in dic:
    url = baseUrl + i
    print(url)
    urllib.request.urlretrieve(url, i)
    print("Downloaded: ", i)
print("Download Complete")
