# 04 - Memeory

Fancy a round of memeory?

When inspecting the DOM tree with developer tools, you can see that the hidden image paths are visible. The following javascript snippet will solve the level and give the egg:
```
var bf = $('.boxFront')

for (i=0;i<100;i++) {
    for (j=i+1;j<100;j++) {
        if (bf[i].src == bf[j].src) {
            bf[j].click(); 
            break;
        }
        
    }
    bf[i].click();
    break;
}
```
After every card has been flipped, we get the following egg:

![egg](egg-memeory.png)
