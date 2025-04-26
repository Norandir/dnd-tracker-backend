import requests

url = "https://www.dnd5eapi.co/graphql/2014"

query = """
query Query {
  monsters {
    name
    armor_class {
      value
    }
    hit_points
  }
}
"""

headers = {"Content-Type": "application/json"}
data = {"query": query, "variables": {}}

response = requests.post(url, json=data, headers=headers)

# Check response status before decoding JSON
if response.status_code == 200:
    try:
        print(response.json())  # Print JSON response
    except requests.exceptions.JSONDecodeError:
        print("Error: Response was not valid JSON")
        print("Response Text:", response.text)
else:
    print(f"Error: Received status code {response.status_code}")
    print("Response Text:", response.text)
