# Ensure that pyjwt and crypto modules are installed.
# pip install pyjwt[crypto]
import jwt
from datetime import timedelta
from datetime import datetime
from datetime import timezone
import json
import os


privateKey = os.environ.get('JWT_PKEY', 'NOT_FOUND')

# print(f'\n The PKEY is : {privateKey} \n')

privateKey = privateKey.encode('ascii')

sub = os.environ.get('JWT_SUB', 'NOT_SET')
aud = os.environ.get('JWT_AUD', 'somesystem-xapi-app')
kid = os.environ.get('JWT_KID', 'SOME_MuleSoft_SOMESYSTEM')

print(privateKey)
print(sub)
print(aud)

validityInHours = int(os.environ.get('JWT_VALIDITY', 336))


cTime = round(datetime.now(tz=timezone.utc).timestamp())
expTime = cTime + (validityInHours * 60 * 60)

jwtPayload = {
    "sub" : sub,
    "aud" : aud,
    "iat" : cTime,
    "exp" : expTime
}

jwtHeader = {
    "alg": "RS256",
    "typ": "JWT",
    "kid" : kid
}

jsonTokenString = json.dumps(jwtPayload)
print(f'\n The JSON body for JWT is : {jsonTokenString} \n')

jwtToken = jwt.encode(jwtPayload, privateKey, algorithm="RS256", headers = jwtHeader)

print(f'\n The JWT Token is : {jwtToken} \n')
