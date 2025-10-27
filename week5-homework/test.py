import requests

# url = "http://127.0.0.1:8000/predict"
# client = {
#     "lead_source": "organic_search",
#     "number_of_courses_viewed": 4,
#     "annual_income": 80304.0
# }
# result = requests.post(url, json=client).json()
# print(result)

url = "http://0.0.0.0:9696/predict2"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
result = requests.post(url, json=client).json()
print(result)