# Name: Lein Chun Hang SID: 55235744 20CS023 Mobile_app_for_monitoring_Traffic_Condition
import requests  
response = requests.get("https://az511.gov/map/Cctv/4250--14")  
file = open("Camelback_rd.jpg", "wb")  
file.write(response.content)  

response = requests.get("https://az511.gov/map/Cctv/4343--14")  
file = open("90th_st.jpg", "wb")  
file.write(response.content)  

response = requests.get("https://az511.gov/map/Cctv/4017--14")  #image resolution concern
file = open("valencia_rd.jpg", "wb")  
file.write(response.content)

response = requests.get("https://az511.gov/map/Cctv/4345--14")  
file = open("via_de_ventura.jpg", "wb")  
file.write(response.content)

response = requests.get("https://az511.gov/map/Cctv/4254--14")  
file = open("northern_ave.jpg", "wb")  
file.write(response.content)

response = requests.get("https://az511.gov/map/Cctv/4081--14")  
file = open("glendale_ave.jpg", "wb")  
file.write(response.content)

file.close()
