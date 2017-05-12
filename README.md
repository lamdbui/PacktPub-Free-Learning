# PacktPub Free Learning Automation Scripts

Experimental scripts used to login to PacktPub and get the free book of the day.

Different implementations with the following methods

- [Selenium](http://www.seleniumhq.org/)
- [requests](https://github.com/kennethreitz/requests)

## Configuration

The script assumes the existence of a local JSON file at $HOME/packtpub.json defined as follows:
~~~
{
    "user": {
        "name": "<YOUR_LOGIN>",
        "password": "<YOUR_PASSWORD>"
    }
}
~~~

NOTE: make sure to set permissions for packtpub.json to only allow access by file creator for security.

~~~
chmod 0600 ~/packtpub.json
~~~

## Usage

Run the scripts with the following command:
~~~
python <selected_script.py>
~~~
