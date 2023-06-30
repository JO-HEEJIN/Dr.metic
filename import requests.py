import requests

url = "http://apis.data.go.kr/1471000/CsmtcsIngdCpntInfoService"
params = {
    "serviceKey": "pkF6Io%2FIoPJuSIgHGnID3o0Ry8i6zUMULBDBBUjS4WbSCIO0YKrF5tBVv1RiCkWUCY7TzkOX%2FcHGQBED7qs%2F2Q%3D%3D",
    # Add other parameters here
}

response = requests.get(url, params=params)
data = response.json()

# Access and use the data returned by the API
# For example, if the data is a list of items:
for item in data:
    # Do something with each item
    print(item)

# Process the data as needed
# Encoding Key
# pkF6Io%2FIoPJuSIgHGnID3o0Ry8i6zUMULBDBBUjS4WbSCIO0YKrF5tBVv1RiCkWUCY7TzkOX%2FcHGQBED7qs%2F2Q%3D%3D

# Decoding Key
# pkF6Io/IoPJuSIgHGnID3o0Ry8i6zUMULBDBBUjS4WbSCIO0YKrF5tBVv1RiCkWUCY7TzkOX/cHGQBED7qs/2Q==