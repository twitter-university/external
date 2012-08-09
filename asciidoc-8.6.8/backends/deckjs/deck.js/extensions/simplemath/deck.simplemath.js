/*!
Deck JS - deck.simplemath
Copyright (c) 2012 Rémi Emonet,
using a modified version of the script from http://gold-saucer.afraid.org/mathml/greasemonkey/ by Steve Cheng
*/

/*
This module provides a support for latex equation syntax.
*/

(function($, deck, undefined) {
    var $d = $(document);
    var may = function(f) {return f ? f : function() {}};
    
    $d.bind('deck.init', function() {
        var container = $[deck]('getContainer');
        $('.latex', container).each(function() {
            var it = this;
            var v = $(it).text();
            it.innerHTML = "$\\displaystyle "+v+"$";
            new latex2mml().patch_element(it);
        });
    });

})(jQuery, 'deck');