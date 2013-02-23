//
// Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
// Released under MIT License
//
var aurora = aurora || []; 

$(document).ready(new function() {
    $("div#loading").hide();
    aurora.options = {
        autoResize: true,
        container: $("#waterfall"),
        offset: 0,
        page: 2,
        ready: true,
        content: '',
    };
    aurora.handler = $("#tiles li");
    aurora.handler.wookmark(aurora.options);
    aurora.page = 2;
    aurora.ready = true;
    aurora.content = '';
    aurora.endless = true;

    aurora.loadmore = function () {
        if ($(window).scrollTop() >= $(document).height() - $(window).height() - 1000){
            if(aurora.ready){
                aurora.ready = false;
                $('#tiles li:last').after(aurora.content);
                if(aurora.handler) 
                    aurora.handler.wookmarkClear();
                aurora.handler = $("#tiles li");
                aurora.handler.wookmark(aurora.options);
                aurora.page ++;
                if(aurora.endless) {
                    $.ajax('/api/homepage_list/' + aurora.page).done(function (data) {
                        if(!(data.length)){
                            aurora.endless = false;
                            aurora.endless = false;
                        } else {
                            aurora.ready = true;
                            aurora.content = data;
                            if ($(window).scrollTop() >= $(document).height() - $(window).height() - 1000){
                                aurora.loadmore();
                            }
                        }
                    });
                }
            }
        }
    }

    $(window).scroll(aurora.loadmore);

    aurora.loadmore();

});
