# UPLOAD ATTACHEMENT INTO SHAREPOINT LIST
import requests
from shareplum import Office365

# Obtain auth cookie
authcookie = Office365('https://YOUR-NAME.sharepoint.com', username='YOUR-USERNAME',password='YOUR-PASSWORD').GetCookies()
session = requests.Session()
session.cookies = authcookie
session.headers.update({'user-agent': 'python_bite/v1'})
session.headers.update({'accept': 'application/json;odata=verbose'})

# dirty workaround.... I'm getting the X-RequestDigest from the first failed call
session.headers.update({'X-RequestDigest': 'FormDigestValue'})
response = session.post(url="https://YOUR-NAME.sharepoint.com/sites/YOU-SITE/_api/web/GetFolderByServerRelativeUrl('YOUR-FOLDER')/Files/add(url='a.txt',overwrite=true)",data="")
session.headers.update({'X-RequestDigest': response.headers['X-RequestDigest']})

# perform the upload
fileName = 'picture.png'
file_name = 'images.png'
with open(file_name, 'rb') as file_input:
    response = session.post(
        url="https://YOUR-NAME.sharepoint.com/sites/YOUR-SITE/_api/web/lists/getbytitle('NAME-LIST')/items(4)/AttachmentFiles/add(FileName='" + fileName + "')",data=file_input)
    print(response.text)

