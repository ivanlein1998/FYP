import requests 
response = requests.get("https://tdcctv.data.one.gov.hk/AID07224.JPG")  
  
file = open("sample_image3.jpeg", "wb")  
file.write(response.content)  
file.close()  

#change AID07224 to any other webcam ID for target webcam
