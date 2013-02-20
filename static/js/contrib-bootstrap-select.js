/*!
 * Convert <select> elements to Dropdown Group
 *  
 * Author: John Rocela 2012 <me@iamjamoy.com>
 */
jQuery(function($){
        $('select').each(function(i, e){
                if (!($(e).data('convert') == 'no')) {
                        $(e).hide().wrap('<div class="btn-group" id="select-group-' + i + '" />');
                        var select = $('#select-group-' + i);
                        var current = ($(e).text()) ? $(e).text(): '&nbsp;';
                        select.before('<input type="hidden" value="' + $(e).val() + '" name="' + $(e).attr('name') + '" id="' + $(e).attr('id') + '" class="' + $(e).attr('class') + '" />');
                        select.html('<a class="btn" href="javascript:;">' + current + '</a><a class="btn dropdown-toggle" data-toggle="dropdown" href="javascript:;"><span class="caret"></span></a><ul class="dropdown-menu"></ul>');
                        $(e).find('option').each(function(o,q) {
                                select.find('.dropdown-menu').append('<li><a href="javascript:;" data-value="' + $(q).attr('value') + '">' + $(q).text() + '</a></li>');
                                if ($(q).attr('selected')) select.find('.dropdown-menu li:eq(' + o + ')').click();
                        });
                        select.find('.dropdown-menu a').click(function() {
                                select.find('input[type=hidden]').val($(this).data('value')).change();
                                select.find('.btn:eq(0)').text($(this).text());
                        });
                }
        });
});

// multiple1902: my modifications:
// put the hidden input before div#select-group-i, because
//   the left-top and left-bottom border radius only applys to 
//   the first element in div#select-group-i, and in the original
//   way, the hidden input is the first element, thus loses the
//   border radius.
