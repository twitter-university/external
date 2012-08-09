# deck.events.js

An extension for [deck.js][] allowing you to execute Javascript when a
  slide becomes/leaves the current, next, or previous slide.

## Requirements

[deck.js][]

## Events

Each event is triggered "on" the slide on which the event occurs (see _Example_)
  and given a single argument -- the direction (see _Direction_)

* **deck.becameCurrent**: Triggered when a slide becomes the current one
  (`to` in `deck.change`).
* **deck.lostCurrent**: The slide is no longer "current"
  (`from` in `deck.change`).
* **deck.becamePrevious**: The slide (by order) just before the current slide.
  (`to - 1` in `deck.change`).
* **deck.becameNext**: The slide (by order) just after the current slide.
  (`to + 1` in `deck.change`).
* **deck.lostPrevious**: The slide (by order) just before the last current slide.
  (`from - 1` in `deck.change`).
* **deck.lostNext**: The slide (by order) just after the last current slide.
  (`from + 1` in `deck.change`).
  

## Direction

Each event is given a direction that helps determine whether the user is
  moving forward or backward in the slide stack. It is provided as an argument
  for the event and can be either `forward` or `reverse`. Essentially:

```
  if(from < to){
    direction = "forward";
  }
  else{
    direction = "reverse";
  }
```


## Example

If you put a placeholder slide `<div id="showGraph" class="slide"></div>` into
  your source, this event will display a Javascript graph when you visit the
  slide (forward) and remove it if you hit the back arrow and return to
  the slide.

```
$("#showGraph").bind('deck.becameCurrent', function(ev, direction) {
  if(direction == "forward"){
    animateGraphIn();
  }
  else{
    animateGraphOut();
  }
});
```


[deck.js]: https://github.com/imakewebthings/deck.js
