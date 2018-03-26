# 08 - Disco Egg

> > Make things as simple as possible but no simpler.
> 
> -- Albert Einstein
> 
> [Click here](https://hackyeaster.hacking-lab.com/hackyeaster/disco/disco.html)

The disco egg keeps changing colors, each cell switching between the
colors defined by classes given to the cell:

```html
<td class="lightgrey yellow tan green red black darkgreen mediumgrey" style="background-color:#DD0907;"></td>
```

It seems like each cell has either white or black as part of their possible colors.
Since we are only interested in the black and white colors, we download the
disco.html and replace the disco script with the following:

```js
$(function(){
    document.querySelectorAll('td.white').forEach(e => {e.style.backgroundColor = '#fff'; });
    document.querySelectorAll('td.black').forEach(e => {e.style.backgroundColor = '#000'; });
});
```

It turns out that each cell does indeed have either a black or a white class and opening
our modified html file reveals the egg for the level:

![egg-8](egg-8.png)
