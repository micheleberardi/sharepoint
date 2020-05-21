from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

# DICT WITH THE INFO THAT YOU NEED TO FILL THE FORM INTO THE LIST
upload_dict = {"ID":4,"ClientName":"JOHN RED","StreetAdrress":"120 BROADWAY","Created":"2020-05-05"}

# Authenticate to Office365 Sharepoint
authcookie = Office365('https://YOUR-NAME.sharepoint.com', username='YOUR-USERNAME',password='YOUR-PASSWORD').GetCookies()
site = Site('https://YOUR-NAME.sharepoint.com/sites/YOUR-SITE/', version=Version.v2016, authcookie=authcookie)
sp_list = site.List('YOUR-LIST')

# GET ALL LIST EXIST OF MY ACCOUNT
sp_data = sp_list.GetListItems()

# CHECK IF LIST IS ALREADY EXIST
sp_dataListItems = sp_list.GetListItems(fields=['ID', 'Title'])
for spResultData in sp_dataListItems:
    id = spResultData.get("ID")
    Title = spResultData.get("Title")

# IF ALREADY EXIST MADE UPDATE OF THE LIST IF DOESNT EXIST MADE NEW LIST
    if id == "1" and Title == 'TEST':
        update_date = [upload_dict]
        sp_list.UpdateListItems(data=update_date, kind='Update')
    else:
        update_date = [upload_dict]
        sp_list.UpdateListItems(data=update_date, kind='New')
