import urllib.request
import json
def predictor(BlueSide,RedSide):
    data = {
            "Inputs": {
                    "input1":
                    [
                        {
                                'Blue Side': BlueSide,   
                                'Red Side': RedSide,   
                        }
                    ],
            },
        "GlobalParameters":  {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/54b725b995124e5b92b9ce215d193c85/services/db5bdeebc0e44d0f95544469b050634a/execute?api-version=2.0&format=swagger'
    api_key = '3llJXg2ID2rmCIoFx8R2mZ64P++IN3PtCfHK41nvWbGU2ONiXda3eJlzy7o+2DaKQk0vtqrMZ/7Xp+S2oc/Pyg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        parsed = json.loads(result.decode("UTF-8"))

        return parsed['Results']['output1'][0]['Score']
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
    
    return 10