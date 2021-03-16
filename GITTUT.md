git clone _link_
_cd into the right folder_

you may use git status to check your changes

git add _file or ._
git commit -m "_message_"
git push origin master / git push (if git push -u origin master was entered before)

---

if repo is not a git repo yet:
git init
_create empty repo in github_
git remote add origin _ssh adress of empty repo_

---

if necessary:

$ git config --global user.name "_real name_"
$ git config --global user.email "_your email_"

---

ssh key generation:

ssh-keygen -t rsa -b 4096 -C "_your email_"
_enter name of key_
_enter passphrase_

show public key with cat _keyname_.pub

---

add key to ssh-agent:
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/_keyname_
