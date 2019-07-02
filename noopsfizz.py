import requests

url = "https://api.noopschallenge.com/fizzbot/questions/1"
while True:
    r=requests.get(url)
    print(r.json()["message"])
    j=r.json()
    j.pop("message")
    print(j)
    if "rules" not in j:
        r=requests.post(url, json={"answer":input()})
    else:
        numsout=""
        for i in j["numbers"]:
            response=""
            for rule in j["rules"]:
                if i%rule["number"] == 0: response+=rule["response"]
            if response=="": response=str(i)
            numsout+=response+" "
        numsout=numsout[:-1] #remove trailing space
        print(j["numbers"])
        print(j["rules"])
        print(numsout)
        r=requests.post(url, json={"answer":numsout})
    print(f"-- {r.json()['result']}! --")
    print(r.json()["message"])
    if r.json()['result'] == "interview complete": exit()
    url="https://api.noopschallenge.com"+r.json()["nextQuestion"]