import json
import re

def extract_paths(data):
    paths = []
    def find_paths(obj, path=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                find_paths(value, path + "/" + key)
        elif isinstance(obj, list):
            for i, element in enumerate(obj):
                find_paths(element, path + "[" + str(i) + "]")
        else:
            paths.append(path)
    find_paths(data)
    return paths

def get_all_data_and_parse(data):
    paths = data.get("paths", {})
    for path in paths:
      print(path)



# call it to get  all schemas
def get_schemas():

    json_file_path = "test.json"
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    try:
        json_data = data

        schemas = json_data.get("components", {}).get("schemas", [])
        schemalist = []
        for schema in schemas:
            schemalist.append(schema)

        schemas_dict=dict()
        for schema in schemalist:
            required=json_data.get("components", {}).get("schemas", []).get(schema, {}).get("required", [])
            schema_values=json_data.get("components", {}).get("schemas", []).get(schema, {}).get("properties", {})
            tuple_list = []
            for key, val in schema_values.items():
                  if key in required:
                      inner_dict = {"name":key,"type":val.get('type'),"placeholder": val.get('title'),"required":True}
                  else:
                      inner_dict = {"name":key,"type":val.get('type'),"placeholder": val.get('title'),"required":False}
                  tuple_list.append(inner_dict)
            
            schemas_dict[schema] = tuple_list
        # print(schemas_dict)
        return schemas_dict

        
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}
    
def get_security_schemas(schema_name):
    json_file_path = "test.json"
    data=""
    securityschemas=""
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    if data: securityschemas=data.get("components", {}).get("securitySchemes", {}).get("securitySchemes", {})
    if securityschemas :return securityschemas.get("type")
    

def get_security_schema(schema_name):
    schemas_dict=get_security_schemas(schema_name)

# call it to give the schema and it will give u schema needed 
def get_schema(schema_name):
    schemas_dict=get_schemas()
    return schemas_dict[schema_name]


def get_all_data_and_parse(data):
    try:
        json_data = json.loads(data)
        paths = json_data.get("paths", [])
        pathlist = []
        for path, methods in json_data.get("paths", {}).items():
            for http_method in methods.keys():
                pathlist.append({"path":path,"http_method":http_method})
        return pathlist
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}



def get_api_info(api_info,method):
    
    pathvariable=[]
    queryparam=[]
    reqbody=[]
    responseschema=[]
    securityparam={}

    json_file_path = "test.json"
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    try: 
        paths = data.get("paths", {}).get(api_info, {})

        # req body
        schema_path=paths.get(method, {}).get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema", {}).get("$ref")
        if schema_path: 
            match = re.search(r'/([^/]+)$', schema_path)
            if match:
               extracted_text = match.group(1)
               reqbody=get_schema(extracted_text)
            else:
               print("No match found")
        
        # response schema
        schema_path=paths.get(method, {}).get("responses", {}).get("200", {}).get("content", {}).get("application/json", {}).get("schema", {}).get("$ref")
        if schema_path: 
            match = re.search(r'/([^/]+)$', schema_path)
            if match:
               extracted_text = match.group(1)
               responseschema=get_schema(extracted_text)
            else:
               print("No match found")


        # path variables or query parameters
        pathvariableparameters=paths.get(method, {}).get("parameters", [])
        for pathvar in pathvariableparameters:
            name=pathvar.get("name")
            required=pathvar.get("required")
            pathorreq=pathvar.get("in")
            type=pathvar.get("schema",{}).get("type")
            placeholder=pathvar.get("schema",{}).get("title")
            onepathvar={"name":name,"required":required,"type":type,"placeholder":placeholder}
            if pathorreq=="query":queryparam.append(onepathvar)
            if pathorreq=="path":pathvariable.append(onepathvar)

        securityparameters=paths.get(method, {}).get("security", [])
        if securityparameters:
            securityparam=securityparameters[0] 
            type=get_security_schema(securityparam)
            print("type",type)
    

        return {"reqbody": reqbody,"pathvariable": pathvariable,"queryparam": queryparam,"securityparameters": securityparam,"responseschema":responseschema}

    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


















##############################response
        # paths = data.get("paths", {}).get(api_info, {})
        # response_schema_path=paths.get("post", {}).get("responses", {})[0].get("content", {}).get("application/json", {}).get("schema", {}).get("$ref")
        # if response_schema_path: 
        #     match_response = re.search(r'/([^/]+)$', response_schema_path)
        #     if match_response:
        #        extracted_text = match_response.group(1)
        #        reqbody=get_schema(extracted_text)
        #        print(reqbody)
        #     else:
        #        print("No match found")