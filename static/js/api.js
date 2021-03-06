function checkbox_counts() {
    var numberOfChecked = $('input:checkbox:checked').length;
    if (numberOfChecked - 3 > 2) {
        $('.lbrr_download_file').hide();
        $('.lbrr_download_zip').css('clip-path','polygon(0 0, 100% 0, 100% 100%, 0 100%)');
        $('.lbrr_download_zip').css('right','200px');
    }
    else if (numberOfChecked - 4 < 2) {
        $('.lbrr_download_file').css('display', 'block');
        $('.lbrr_download_zip').css('clip-path','polygon(0 0, 100% 0, 100% 100%, 10px 100%)');
        $('.lbrr_download_zip').css('right','95px');
    }

}

function get_post(url) {
    $.ajax({
        type: 'GET',
        url: url,
        success: function (data) {

            $('.ne_block_news').html('');
            for (i = 0; i < data.text.length; i++) {

                var tag = data.tag[i];
                $('.ne_block_news').append('<div class="ne_main_news">' +
                    '<div class="ne_news_img">' +
                    '<img src="' + data.image[i] + '" alt="">' +
                    '</div>' +
                    '<div class="ne_news_text">' +
                    '<div class="ne_news_parag">' +
                    '<a href="' + data.url[i] + '">' + data.title[i] + '</a>' +
                    '</div>' +
                    '<div id="{{ new.id }}" class="ne_news_short_art">' +
                    $(data.text[i]).text().slice(0, 155) + '...' +
                    '</div>' +

                    '<div class="ne_news_tags">' +
                    'Теги:' +
                    '<div class="ne_news_tags_tg">' +
                    tag + '</div>' +
                    '</div>' +
                    '<div class="ne_news_date_pub">' +
                    'Опубликованно:' +
                    '<div class="ne_news_public_date">' + new Date(data.date[i]).toLocaleString('ru', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                        hour: 'numeric',
                        minute: 'numeric'

                    }) + '</div>' +
                    '</div>' +
                    '</div>' +
                    '<div class="ne_but_more">' +
                    '<a href="' + data.url[i] + '">Читать далее</a>' +
                    '</div>')
            }
        }

    })
}


function get_journals(form, course) {
    var elements = document.getElementsByName('universities');
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].checked)
            var institute = (elements[i].value);
    }
    $.ajax({
        url: '/api/v0/get_journals/' + institute + '/' + form + '/' + course + '/',
        type: 'GET',
        success: function (data) {
            $('.journal').hide();
            if (data.groups.length >= 1)
                for (i = 0; i < data.groups.length; i++) {
                    $('.journ_win_rate').append('<div class="journal">' +
                        '<div class="journal_circle"></div>' +
                        '<div class="journal_backg_n">' +
                        '<div class="journal_name">' +
                        '<a class="permission_link" href="' + data.links[i] + '" target="jframe" onclick="permisiion_journal(this.getAttribute(\'href\'))">' + data.groups[i] + '</a>' +
                        '</div>' +
                        '</div>' +
                        '</div>');
                }

            else if (data.groups.length === 0) {
                $('.journal').hide()
            }
        }
    })
}

function get_materials(discipline) {
    discipline = discipline.replace(/^\s*/, '');
    $.ajax({

        type: 'GET',
        url: '/api/v0/get_materials/' + discipline,
        success: function (data) {

            $('.lib_frame').html('');
            $('.lib_frame').append('<label><input type="checkbox" style="margin-right: 15px;" onClick="toggle(this)"/>'+'<a style="color: #000;">'+'Выбрать все'+'</a>' +'</label>'+'<br/>');
            for (i = 0; i < data.names.length; i++) {

                $('.lib_frame').append('<input  style="display: ' +
                    'none;" type="text" name="discipline" value="' +
                    discipline + '">' +  '<label>'+'<input style="margin-right: 15px;" ' +
                    'type="checkbox" class="material_check" name="foo" value="' +
                    data.file_urls[i] + '"  id="foo" onclick="checkbox_counts()">'  +'<a style="color: #000;">'+ data.names[i] +'</a>' +'</label>' +
                    '<br/>');

            }
        }


    })
}


function submit_form() {
    document.getElementById("lib_form").submit();
}

function submit_form_file() {

    $('.lib_frame').append('<input type="text" style="display:none" name="file" value="true"/>');
    document.getElementById("lib_form").submit();
}