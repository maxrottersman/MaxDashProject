Read me to come...

Started repo on PC with a .gitignore file, readme.MD and created a Visual Code workspace in folder "HomePC.code-workspace" which should be ignored from .gitignore.  Then ran

$ git init
$ git add .
$ git commit -m "First commit"
$ git remote add origin https://github.com/maxrottersman/MaxDashProject.git

Tested with
$ git remote -v

$ git push origin master
    but came back with errors. "Fatal: HttpRequestException encountered.
"  However repo seems okay on github

Now testing VC git synch with the text added above...worked (commit 3)

Trying Virtualenv

python -m venv .venv

then added .venv/* to .gitignore

in case I have to do manually, something like
source venv/bin/activate
deactivate

