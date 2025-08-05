# avenga_qa_test

running manually on linux:
1. create venv if needed<br>
`mkdir venv`<br>
`virtualenv venv/`<br>
`source venv/bin/activate`<br>
2. install requirements: `pip install -r requirements.txt`
3. install allure cli using package manager, e.g. `yay -S allure-commandline`<br>
you can find details here: `https://github.com/allure-framework/allure2/releases/`
4. run test using command `python main.py run`
5. to run specific test or pass markers use command <br>
`python main.py run --marker marker` <br>
e.g. `python main.py run --marker books`
6. Report will be generated automatically<br>To see it, run console command:<br>
`allure open <path_to_repo>/report`
To open it in your browser, see the docs: `https://allurereport.org/docs/gettingstarted-view-report/`

available markers:
- books
- authors
