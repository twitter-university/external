/*!
Deck JS - deck.svg
Copyright (c) 2012 Rémi Emonet, as a major refactor from an early version from Rémi Barraquand.
*/

/*
This module provides a support for managed svg inclusion (allowing proper DOM access subsequently for animations, etc.).
*/

(function($, deck, undefined) {
    var $d = $(document);
    var may = function(f) {return f ? f : function() {}};

    $.extend(true, $[deck].defaults, {
        classes: {
            svgPlaceholder: 'deck-svg'
        }
    });

    /*
      jQuery.deck('Init')
    */
    $d.bind('deck.init', function() {
        var opts = $[deck]('getOptions');
        var container = $[deck]('getContainer');

        /*
          Load parameters from an Object element
        */
        var loadObjectParams = function(objectElement) {
            var attributes = {};
            $(objectElement).children("param").each(function(index){
                attributes[$(this).attr("name")] = $(this).attr("value");
            });
            return attributes;
        }
        
        /*
          Return true if default params are set.
        */
        var validateParams = function(params) {
            return params['src'];// && params['width'] && params['height'];// && params['animator'];
        }
        
        /*
          Create SVG placeholder
        */
        var createSVG = function(object, attributes) {
            var $canvas, $control, $next, $reload, $placeholder;
            
            /* Create svg canvas */
            $canvas = $("<div />").attr({
                'id':  $(object).attr('id'),
                'class': opts.classes.svgPlaceholder + " " + $(object).attr('class')
            }).css({
                'height': attributes['height'],
                'width': attributes['width']
            });
            return $canvas;
        }

        
        /* Go through all toplevel slides */
        $($[deck]('getSlides')).each( function(i, $el) {
            var $slide = $[deck]('getSlide', i);

            /*
            if ($slide.has("object[type='deckjs/svg']").length>0) {
                $slide.data('animators', new Array());
            }*/
            
            /* Find all the object of type deckjs/svg */
            if ($slide == null) return true;
            $slide.find("object[type='deckjs/svg']").each(function(index, obj) {
                //var id = $(this);
                /* Load attributes and validate them */
                var attributes = loadObjectParams(obj);
                if (!validateParams(attributes) ) {
                    throw "Error while initializing "+$(obj).attr('id')+", please ensure you have setup the required parameters."
                    return false;
                }
                
                /* Add this animator to the list of animators of the current slide. */
                //$slide.data('animators').push(attributes['animator']);
                
                /* Create SVG placeholder */
                var SVG = createSVG(obj, attributes);
                $(obj).replaceWith(SVG);
                
                // Finaly load the SVG data
                //$[deck]('addLoading');
                SVG.svg({
                    loadURL: attributes['src'],
                    onLoad: function($svg, w, h) {
                        var aa = $($svg.root());
                        if (aa.attr('viewBox') == undefined) {
                            var to = "0 0 " + w + " " + h;
                            $svg.root().setAttribute("viewBox", to);
                            aa.attr("svgViewBox", to);
                            if (attributes['stretch'] == 'true') $svg.root().setAttribute('preserveAspectRatio', "none");
                        }
                        /*
                          $[deck]('removeLoading')
                        */
                    }
                });
            });
        });
    })
    
    
})(jQuery, 'deck');

