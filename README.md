# PacktPub Free Learning Automator

Experimental Selenium script to login to PacktPub and get the free book of the day.

## Configuration

The script assumes the existence of a local JSON file at $HOME/packtpub.json
'''
{
    "user": {
        "name": "<YOUR_LOGIN>",
        "password": "<YOUR_PASSWORD>"
    }
}
'''

NOTE: make sure to set permissions for packtpub.json to only allow access for file creator.

'''
chmod 0600 ~/packtpub.json
'''
