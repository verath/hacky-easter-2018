# 16 - git cloak --hard

> This one requires your best Git-Fu! Find the hidden egg in the repository.
> 
> `repo.zip`

Unzip and cd into the repository we first check the git log and reflog:

```
> git log --oneline --no-decorate
b9e860f even more funny images added
3839c14 more funny images added
228b603 created the funny git meme repo

> git reflog --no-decorate
b9e860f HEAD@{0}: commit: even more funny images added
3839c14 HEAD@{1}: checkout: moving from branch to master
9a29769 HEAD@{2}: commit: branch created
3839c14 HEAD@{3}: checkout: moving from master to branch
3839c14 HEAD@{4}: commit: more funny images added
228b603 HEAD@{5}: checkout: moving from temp to master
9d7c9b5 HEAD@{6}: commit: added one more image
b9820d5 HEAD@{7}: commit: temp branch created
228b603 HEAD@{8}: checkout: moving from master to temp
228b603 HEAD@{9}: commit (initial): created the funny git meme repo
```

Doing some manual labour we can checkout each unique commit and look at the
images at that time. This gives us nothing more than another false egg.


Perhaps then the file is no longer reachable? `git fsck` makes it
easy to check for, and recover, unreachable files:

```
> git fsck --unreachable
Checking object directories: 100% (256/256), done.
unreachable blob dbab6618f6dc00a18b4195fb1bec5353c51b256f

> git fsck --lost-found
Checking object directories: 100% (256/256), done.
dangling blob dbab6618f6dc00a18b4195fb1bec5353c51b256f
dangling commit 9d7c9b5a1c8773ea48caac90d05401679b0a8897 
```

The blob "dbab6618f6dc00a18b4195fb1bec5353c51b256f" is then put into the
`.git\lost-found\other` directory. Opening it as an image and sure enough,
the dangling blob was our egg:

![egg16](dbab6618f6dc00a18b4195fb1bec5353c51b256f.png)
