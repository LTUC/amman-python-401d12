# Notes

## Create Environment Using Windows PowerShell

```bash
python -m venv .venv

.venv\Scripts\activate

pip install package-name

```

### Github for Windows

* [install git for windows](https://gitforwindows.org/)

* When you've successfully started the installer, you should see the Git Setup wizard screen. Follow the Next and Finish prompts to complete the installation.
* open windows powershell and run these commands

```bash
git config --global user.name "username"
git config --global user.email "your email"
```

* create new empty repository named tkinter
run these commands

> **clone your repo using https**

```bash
echo "# tt" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin your https link
git push -u origin main
```

* how to Remove .git file if you want to create new one using https

* ``Remove-Item -force .git``