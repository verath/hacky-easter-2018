# 06 - Cooking for Hackers

> You've found this recipe online:
> 
> 1 pinch: c2FsdA==
> 
> 2 tablesspoons: b2ls
> 
> 1 teaspoon: dDd3Mmc=
> 
> 50g: bnRkby4=
> 
> 2 medium, chopped: b25pb24=
> 
> But you need one more secret ingredient! Find it!

The ingredients are base64 encoded. Decoding them reveals a
[.onion](https://en.wikipedia.org/wiki/.onion) URL:

```js
> ["c2FsdA==", "b2ls", "dDd3Mmc=", "bnRkby4=", "b25pb24="].map(x => atob(x)).join("")
"saltoilt7w2gntdo.onion"
```

Visiting [saltoilt7w2gntdo.onion](saltoilt7w2gntdo.onion) in the Tor browser gives us
the egg for the level:

![egg 6](ingredient_egg06.png)
