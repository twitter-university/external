/*!
Deck JS - deck.clone
Copyright (c) 2011 Remi BARRAQUAND
Dual licensed under the MIT license and GPL license.
https://github.com/imakewebthings/deck.js/blob/master/MIT-license.txt
https://github.com/imakewebthings/deck.js/blob/master/GPL-license.txt
*/

/*
This module provides a support for cloning the deck.
*/

(function($, deck, undefined) {
    var $d = $(document);
    var clones = new Array();
        
    $.extend(true, $[deck].defaults, {	
        selectors: {
            clonepointer: ".clonepointer"
        },
        classes: {
            hasClones: 'has-clones'
        },
        keys: {
            clone: 67 // c
        }
    });

    var cleanClones = function() {
        var opts = $[deck]('getOptions');
        // remove closed windows
        $.each(clones, function(index, clone) {
            if (clone.closed()) {
                clones.splice(index, 1); // remove element "index"
            }
        });
        // tag/untag the current container depending on the presence of clones
        if (clones.length > 0) {
            $("body").addClass(opts.classes.hasClones);
        } else {
            $("body").removeClass(opts.classes.hasClones);
        }
    };
    /*
	jQuery.deck('addClone')
	
	Create a clone of this window and add it to the clones list.
	*/
    $[deck]('extend', 'addClone', function() {
        clone = new DeckClone();
        clones.push(clone);
        cleanClones();
        return clone;
    });
    $[deck]('extend', 'pointerAt', function(rx, ry) {
        var opts = $[deck]('getOptions');
        var r = $(".deck-current").get(0).getBoundingClientRect();
        var x = r.left + r.width * rx;
        var y = r.top + r.height * ry;
        var pos = {left: x, top: y};
        var current = $(".deck-current").get(0);
        var pointers = $(opts.selectors.clonepointer);
        if (pointers.get(0).parentNode != current) { // move them within the new slide if it changed
            pointers.show().appendTo(".deck-current");
        }
        pointers.offset(pos);
    });
      
    /*
        jQuery.deck('Init')
        */
    $d.bind('deck.init', function() {
        var opts = $[deck]('getOptions');
        var container = $[deck]('getContainer');
        
        $(opts.selectors.clonepointer).hide();

        /* Bind key events */
        $d.unbind('keydown.deckclone').bind('keydown.deckclone', function(e) {
            if (e.which === opts.keys.clone || $.inArray(e.which, opts.keys.clone) > -1) {
                $[deck]('addClone');
                e.preventDefault();
            }
        });
    })
    /* Update current slide number with each change event */
    .bind('deck.change', function(e, from, to) {
        var opts = $[deck]('getOptions');
        var slideTo = $[deck]('getSlide', to);
        var container = $[deck]('getContainer');
        cleanClones();
        $.each(clones, function(index, clone) {
           clone.deck('go', to);
        });
    })
    /* Do the animations locally */
    .bind('deck.step', function(e, delta) {
        cleanClones();
        $.each(clones, function(index, clone) {
            if (delta == -1) clone.deck('stepPrev');
            else if (delta == 1) clone.deck('stepNext');
        });
    })
    /* Replicate mouse cursor */
    .bind('mousemove', function(e) {
        var r = $(".deck-current").get(0).getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width;
        var y = (e.clientY - r.top) / r.height;
        cleanClones();
        $.each(clones, function(index, clone) {
            clone.deck('pointerAt', x, y);
        });
    });
    
    /*
        Simple Clone manager (must be improved, by for instance adding cloning
        option e.g. propagate change, etc.)
        */
    var DeckClone = function() {
        var clone = window.open(window.location);
        this.closed = function() {return clone.closed;}
        this.deck = function() {
            if (clone.closed) return;
            if (clone['$']) clone['$'].deck.apply(clone['$'], arguments)
        }
    }
})(jQuery, 'deck');