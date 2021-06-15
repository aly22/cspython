# import requests_cache
import requests
import json
import webbrowser
# page = requests.get("https://api.datamuse.com/words?rel_rhy=cat")
# print(type(page))
# print(page.text[:150]) # print the first 150 characters
# print(page.url) # print the url that was fetched
# print("------")
# x = page.json() # turn page.text into a python object
# print(type(x))
# print("---first item in the list---")
# print(x[0])
# print("---the whole list, pretty printed---")
# print(json.dumps(x, indent=2)) # pretty print the results
def get_flickr_data(tags_strings):

    params_d={}
    paras=['api_key','fe4e8304d5c0ffc4489b0017745eaa78','method','flickr.photos.search','tags',tags_strings,'per_page',10,'format','json','nojsoncallback',1]
    for idx in range(0,len(paras)-1,2):
        params_d[paras[idx]]=paras[idx+1]
    baseurl = "https://api.flickr.com/services/rest/"
    flickr_response=requests.get(baseurl,params=params_d)

    print(flickr_response.url)
    return flickr_response.json()
raw_file=get_flickr_data('nature,landscape')
def get_data(jsondata):
    print(json.dumps(jsondata,indent=2))
    photos=[]
    for photo in jsondata["photos"]["photo"]:
        photo_id=photo['id']
        user_id=photo["owner"]
        photos.append(f"https://www.flickr.com/photos/{user_id}/{photo_id}")
        photo=f"https://www.flickr.com/photos/{user_id}/{photo_id}"
        webbrowser.open_new_tab(photo)
    return photos
get_data(raw_file)