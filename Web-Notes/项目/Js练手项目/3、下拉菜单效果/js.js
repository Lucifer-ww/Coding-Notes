/**
 * ---------------------------------------------
 * Javscript is just for make elements clickable
 * Effects are on the css only
 * ---------------------------------------------
 * @since 2015/06/10
 * @author Reiha Hosseini ( @mrReiha )
 */
;
!(function (w, d) {

    'use strict';

    var titles = d.querySelectorAll('.title'),

        i = 0,
        len = titles.length;

    for (; i < len; i++)
        titles[i].onclick = function (e) {

            for (var j = 0; j < len; j++)
                if (this != titles[j])
                    titles[j].parentNode.className = titles[j].parentNode.className.replace(/ open/i, '');

            var cn = this.parentNode.className;

            this.parentNode.className = ~cn.search(/open/i) ? cn.replace(/ open/i, '') : cn + ' open';

        };

})(this, document);