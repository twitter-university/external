(function($, deck, undefined) {
   $(document).bind('deck.change', function(e, from, to) {
      var $prev = $[deck]('getSlide', to-1),
      $next = $[deck]('getSlide', to+1),
      $oldprev = $[deck]('getSlide', from-1),
      $oldnext = $[deck]('getSlide', from+1);
      
      direction = "forward";
      if(from > to){
        direction = "reverse";
      }

      $[deck]('getSlide', to).trigger('deck.becameCurrent', direction);
      $[deck]('getSlide', from).trigger('deck.lostCurrent', direction);

      $prev && $prev.trigger('deck.becamePrevious', direction);
      $next && $next.trigger('deck.becameNext', direction);

      $oldprev && $oldprev.trigger('deck.lostPrevious', direction);
      $oldnext && $oldnext.trigger('deck.lostNext', direction);
   });
})(jQuery, 'deck');

