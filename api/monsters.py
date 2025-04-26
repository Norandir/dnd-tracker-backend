from fastapi import APIRouter
import httpx

# Create an APIRouter instance
router = APIRouter()

# GraphQL API that orginal infomation is pulled from
GRAPHQL_API_URL = "https://www.dnd5eapi.co/graphql/2014"

#router for /monsters 
@router.get("/monsters")
async def get_monsters():
    query = """
    query {
      monsters {
        name
        armor_class {
          value
        }
        hit_points
      }
    }
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(GRAPHQL_API_URL, json={"query": query})

        # Print status code and raw response for debugging
        print("STATUS CODE:", response.status_code)
        print("RAW RESPONSE:", response.text)

        data = response.json()

    #Format the infomation so it matches the frontend
    formatted_monsters = [
        {
            "name": monster["name"],
            "HP": monster["hit_points"],
            "AC": monster["armor_class"][0]["value"] if monster["armor_class"] else 0
        }
        for monster in data.get("data", {}).get("monsters", [])
    ]

    return {"monsters": formatted_monsters}