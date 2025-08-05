# avenga_qa_test

running manually on linux:
1. create venv if needed<br>
`mkdir venv`<br>
`virtualenv venv/`<br>
`source venv/bin/activate`<br>
2. install requirements: `pip install -r requirements.txt`<br>
3. install allure cli using package manager, e.g. `yay -S allure-commandline`<br>
more installation instructions `https://allurereport.org/docs/install-for-linux/`
4. run test using command `python main.py run`
5. to run specific test or pass markers use command <br>
`python main.py run --marker marker` <br>
e.g. `python main.py run --marker books`
6. Reports in html format will be generated automatically and stored in reports/ directory
7. CI/CD is configured in github actions and enabled on push, pull request and on manuall trigger with Require approval for all external contributor option enabled. 

available markers:
- books
- authors
