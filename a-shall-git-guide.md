# Git Guide for a-Shell (iOS)

A practical guide to using Git inside the a-Shell terminal app on iPhone/ iPad.

------------------------------------------------------------------------

## 1. Initial Setup

### Install a-Shell

Download **a-Shell** from the App Store.

------------------------------------------------------------------------

## 2. Configure Git (First Time Only)

Set your Git identity:

``` bash
git config --global user.name "Ryota12348"
```

```bash
git config --global user.email "takatakaoni926@gmail.com"
```

Make sure the email matches your GitHub account.

------------------------------------------------------------------------

## 3. Clone a Repository

Copy the HTTPS URL from GitHub:

``` bash
git clone https://github.com/Ryota12348/my-log.git
```

Move into the directory:

``` bash
cd my-log
```

------------------------------------------------------------------------

## 4. Editing Files

Use nano (recommended for beginners):

``` bash
nano README.md
```

Or vim:

``` bash
vim README.md
```

You can also edit files using the iOS Files app.

------------------------------------------------------------------------

## 5. Check Status

``` bash
git status
```

Shows modified files.

------------------------------------------------------------------------

## 6. Add Changes

``` bash
git add .
```

Or add a specific file:

``` bash
git add README.md
```

------------------------------------------------------------------------

## 7. Commit

``` bash
git commit -m "Update README"
```

------------------------------------------------------------------------

## 8. Push to GitHub

``` bash
git push
```

Note: GitHub requires a **Personal Access Token (PAT)** instead of a
password.

Create one in: Settings  Developer settings Personal access tokens

------------------------------------------------------------------------

## 9. Pull Latest Changes

``` bash
git pull
```

------------------------------------------------------------------------

## 10. Useful Commands Summary


  Command      Purpose
  ------------ ---------------------
  git clone    Download repository
  git status   Check changes
  git add      Stage changes
  git commit   Record changes
  git push     Upload changes
  git pull     Download updates

------------------------------------------------------------------------

## Recommended Daily Workflow

Morning:

``` bash
git pull
```

After editing:

``` bash
git add .
git commit -m "Daily update"
git push
```

------------------------------------------------------------------------

## Tips

-   Commit frequently.
-   Keep commit messages clear.
-   Use private repositories for personal logs.
-   Small commits are better than large ones.

------------------------------------------------------------------------

*End of guide.*
