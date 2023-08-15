# FACEBOOK KOMENTAR - WITH TERMUX
<div align="center">
  <img src="Data/Comments.png">
  <br>
  <br>
  <p>
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/rozhakxd/Comments">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/rozhakxd/Comments">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/rozhakxd/Comments">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/rozhakxd/Comments">
    <img alt="Maintenance" src="https://img.shields.io/maintenance/no/2023">
  </p>
  <h4> Facebook Comments Homepage Using Termux Only ! </h4>
</div>

##

### What is Comments?
[**Comments**](https://github.com/RozhakXD/Comments) Is a script to comment on and like all posts on the home page using an image containing the name of the target account.

### Termux command?
First you must have the [Termux](https://f-droid.org/repo/com.termux_118.apk) application to run this script and for how to use it can be seen on [**Youtube**](https://youtu.be/cltn7d6kX2g). Then you enter some basic commands below!
```
$ apt update -y && apt upgrade -y
$ pkg install git python-pip
$ git clone https://github.com/RozhakXD/Comments
$ cd "Comments"
$ python -m pip install -r requirements.txt
$ python Run.py
```

```
$ cd "$HOME/Comments" && git pul
$ python Run.py
```

### Why the error when commenting?

- There may be a problem when creating the image resulting in an error.
- The script is looking for an appropriate image to comment on.
- Use comments from the website **"https://textpro.me"** so that there are not too many errors.

### Why login failed?

- Your facebook account is logged out or checkpoint.
- Your facebook account is in free mode.
- Your facebook account is locked or checkpoint new version.

### Facebook temporarily locked?

- Don't run comments and reactions too often, you can rest if 50 comments have been sent
- I hope you use more than 60 seconds delay.
- The account is in an online state in the browser taking cookies.

### Why can't comments be in groups?
Picture comments often make mistakes in groups, so this script only sends pictorial comments on posts other than the Facebook group and for group posts can only be liked or reacted.

##
```python
print("Good luck hope it works!")
```
##
