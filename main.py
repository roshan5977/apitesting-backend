
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
import json
import services
from fastapi.middleware.cors import CORSMiddleware
import httpx
import aiohttp 

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

# Cors error handling
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Test
@app.get("/")
def test():
    return {"status": "success"}

@app.post("/uploadapiinfo/")
async def upload_json(file: UploadFile):
    if file.filename.endswith(".json"):
        contents = await file.read()
        
        # Write the contents directly to "test.json"
        with open("test.json", "wb") as json_file:
            json_file.write(contents)
        
        # Now you can use the contents for processing
        extracted_data = services.get_all_data_and_parse(contents)
        return JSONResponse(content=extracted_data, status_code=200)
    else:
        return JSONResponse(content={"error": "File must have a .json extension"}, status_code=400)



@app.post("/getapiinfo/")
async def get_api_info(api_info:str,http_method:str):
   return services.get_api_info(api_info,http_method)



# now using playwright request
# from playwright.sync_api import sync_playwright
import requests  

# Define your schema validation function (you can use a different library for this)
def validate_response(response, expected_schema):
    # Perform schema validation here
    # Example using 'requests' and 'jsonschema'
    try:
        response_json = response.json()
        print("response ",response_json)
        print("expected response ",expected_schema)
        # Validate 'response_json' against 'expected_schema'
        # Implement your validation logic here
        # Example:
        # jsonschema.validate(response_json, expected_schema)
        return True
    except Exception as e:
        return False
    
# for making it asynchronous 
# @app.post("/makerequest/")
# async def api_request(method, path, url, req_body=None):
  
#     is_valid = ""

#     async with aiohttp.ClientSession() as session:
#         async with session.request(method, url, json=req_body) as response:
#             print("response",response)
#             print("response status",response.status)

#             # Validate the response against the expected schema
#             # expected_schema = services.get_schema(path)
#             # expected_schema="ok"
#             # if expected_schema:
#             #     is_valid = validate_response(response, expected_schema)
#             #     if is_valid:
#             #         print(f"{method} request to {url} PASSED schema validation.")
#             #     else:
#             #         print(f"{method} request to {url} FAILED schema validation.")

#     return "passed"




# for making it synchronous 
import requests
@app.post("/makerequest/")
def api_request(method: str, path: str, url: str, req_body: dict = None):
    is_valid = ""

    print("Request body",req_body)
    print("url",url)
    try:
        response = requests.request(method, url, json=req_body)

        print("Response Status:", response.status_code)
        response_text = response.text
        print("Response Body:", response_text)

        if response.status_code == 422:
            print("Request was unprocessable. Check the response body for more details.")
            return {'status':"422","respose body": response.text}
        if response.status_code == 200 or response.status_code == 201:
            return {"status": response.status_code,"respose body": response.text}

    except Exception as e:
        print(f"Error making the request: {e}")
    return {"status": response.status_code,"respose body": response.text}







if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)























# #Extracted from: https://playwright.dev/python/docs/api/class-apirequestcontext#api-request-context-get

# import asyncio
# from playwright.async_api import async_playwright, Playwright

# async def run(playwright: Playwright):
#     # This will launch a new browser, create a context and page. When making HTTP
#     # requests with the internal APIRequestContext (e.g. `context.request` or `page.request`)
#     # it will automatically set the cookies to the browser page and vise versa.
#     # browser = await playwright.chromium.launch()
#     # context = await browser.new_context(base_url="https://api.github.com")
#     # api_request_context = context.request
#     # page = await context.new_page()

#     # Alternatively you can create a APIRequestContext manually without having a browser context attached:
#     api_request_context = await playwright.request.new_context(base_url="http://localhost:3000")
#     data = {
#         "completed": False,
#         "title": "test",
#         "id": "500",
#     }

#     # Create a repository.
#     response = await api_request_context.post(
#         "/todos",
#         data=data,
#     )
#     assert response.ok
#     print(f"todo Var: {response}")

# async def main():
#     async with async_playwright() as playwright:
#         await run(playwright)

# asyncio.run(main())