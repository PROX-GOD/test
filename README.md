import requests

import uuid

app_id = "YOUR APP ID"

app_secret = "YOUR SECRET KEY"

# Step 1: Get short-lived access token

url = f"https://graph.facebook.com/oauth/access_token?client_id={app_id}&client_secret={app_secret}&grant_type=client_credentials"

response = requests.get(url)

token_data = response.json()

access_token = token_data["access_token"]

# Step 2: Generate headers and data

adid = str(uuid.uuid4())

gtt = "Samsung Galaxy S10"

gttt = str(uuid.uuid4())

application_version = "555.0.0.123"

application_version_code = "123456789"

android_version = "11"

fb_api_caller_class = "com.facebook.account.login.protocol.Fb4aAuthHandler"

fb_api_req_friendly_name = "authenticate"

locale = "es_CU"

client_country_code = "CU"

device_id = str(uuid.uuid4())

source = "device_based_login"

error_detail_type = "button_with_disabled"

generate_session_cookies = "1"

generate_analytics_claim = "1"

generate_machine_id = "1"

format = "json"

credentials_type = "device_based_login_password"

method = "auth.login"

data = {

    "adid": adid,

    "password": "mypassword123",

    "email": "myemail@example.com",

    "cpl": "true",

    "credentials_type": credentials_type,

    "source": source,

    "error_detail_type": error_detail_type,

    "format": format,

    "generate_session_cookies": generate_session_cookies,

    "generate_analytics_claim": generate_analytics_claim,

    "generate_machine_id": generate_machine_id,

    "locale": locale,

    "client_country_code": client_country_code,

    "device": gtt,

    "device_id": device_id,

    "method": method,

    "fb_api_req_friendly_name": fb_api_req_friendly_name,

    "fb_api_caller_class": fb_api_caller_class,

}

headers = {

    "Content-Type": "application/x-www-form-urlencoded",

    "User-Agent": f"Davik/2.1.0 (linex; U; Android {android_version}.0.0; {gtt} Build/{gttt} [FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/{{density=2.0,width=720,height=1280}};FBLC/{locale};FBRV/{application_version_code};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{gtt};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]",

    "Authorization": f"Bearer {access_token}",

}

# Step 3: Send request with generated data and headers

url = "https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true"

response = requests.post(url, data=data, headers=headers, allow_redirects=False)

print("Request data:", data)

print("Request headers:", headers)

print("Response text:", response.text)
