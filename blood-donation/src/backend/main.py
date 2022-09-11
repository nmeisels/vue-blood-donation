import requests
import json
import uvicorn

from requests.structures import CaseInsensitiveDict
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

MADA_URL = "https://www.mdais.org/umbraco/api/invoker/execute"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=None,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/get-data")
def get_data() -> dict:
    headers = CaseInsensitiveDict()
    headers["authority"] = "www.mdais.org"
    headers["sec-ch-ua"] = """" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99" """
    headers["dnt"] = "1"
    headers["accept-language"] = "he"
    headers["sec-ch-ua-mobile"] = "?0"
    headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, " \
                            "like Gecko) Chrome/99.0.4844.84 Safari/537.36 "
    headers["content-type"] = "application/json"
    headers["accept"] = "application/json, text/plain, */*"
    headers["sec-ch-ua-platform"] = "\"macOS\""
    headers["origin"] = "https://www.mdais.org"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-dest"] = "empty"
    headers["referer"] = "https://www.mdais.org/blood-donation"
    headers["cookie"] = "_ga=GA1.2.1698825273.1637841226; _fbp=fb.1.1637841226441.19954475; GCLB=CMuT68yTs7z6xAE; " \
                        "_gac_UA-24996870-1=1.1647332460.CjwKCAjw8sCRBhA6EiwA6_IF4Yrpkz8zbC_zbqueVJ9xQsSIE5" \
                        "-Ut3xnlD-doB2LUAWJrkGtVJrbsBoCqG4QAvD_BwE; __atssc=google%3B11; " \
                        "rbzid=wTUy/MCWPbEze27/q474mUvgL9" \
                        "+iw6ZKPwoMoEJuvcaiOjiJtRAnAOuTuIOK3z42nWFgs6h6jnwJJutlaEpoY1wyKLit2HeXYNdC46lwbeWP1Orm6hpnREN7du0941CIyneZdPonOOME3h9KacD0DuCQvejcFjejtsJqx0N8r/q9d1w5jgmrmWWsCC3fHUZqGsb4E5j/71RiOLQJCkJBNmE1SLB8JXmpq5GhSar/5dx/Jy9ddQx2GfT1SLwh+tJu; rbzsessionid=7c39416851351028a35fee43a1a9f74b; _gid=GA1.2.1852248166.1649138329; __atuvc=1%7C10%2C18%7C11%2C0%7C12%2C0%7C13%2C3%7C14; __atuvs=624bda9cfc8f12f3002; _gat_gtag_UA_24996870_1=1 "

    data = '{"RequestHeader":{"Application":101,"Module":"BloodBank","Function":"GetAllDetailsDonations",' \
           '"Token":""},"RequestData":""} '

    resp = requests.post(MADA_URL, headers=headers, data=data)

    print(resp.status_code)
    response = resp.json()
    response_dict = json.loads(response["Result"])
    return response_dict


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10010, debug=True)
