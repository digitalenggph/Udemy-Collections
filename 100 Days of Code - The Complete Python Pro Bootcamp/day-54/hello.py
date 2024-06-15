"""`
DAY-54 NOTES
    LESSON 1:
    * pwd   - print working directory
    * ls    - list all files and folders in current directory
    * cd    - change directory
    * mkdir - make directory
    * touch - creates file (did not work though)
    * echo  - creates file [echo > main.py]
    * rm    - removes files and folders
                -rf     - flag (dash) rf
                        - recursively deletes everything

    LESSON 2:
    __name___
`"""

# save this as hello.py

print(__name__)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run()
