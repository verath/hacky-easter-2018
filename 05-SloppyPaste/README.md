# 05 - Sloppy & Paste

> This is a mobile challenge. Check it out in the Hacky Easter app!

After [extracting the APK](https://github.com/verath/hacky-easter-2017/blob/master/extract-apk.md) we find the
source for this level in `assets\www\challenge05.html`. It consists of a textarea with the base64-encoded
egg of the level. There also seems to be event listeners for when the text is copied, presumably to modify
the copied data in some way. But since we have access to the source, we can simply copy paste directly from
the HTML file circumventing any such event trickery. 

Interpreting the egg data as a base64-encoded image (`<img src="data:image/png;base64, ...">`)
we find the egg for the level:

![egg5](egg5.png)
