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
                    data.text[i].slice(7, 200) + '...' +
                    '</div>' +

                    '<div class="ne_news_tags">' +
                    'Теги:' +
                    '<div class="ne_news_tags_tg">'+
                   tag+'</div>' +
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
                    '<a href="' + data.url + '">Читать далее</a>' +
                    '</div>')
            }
        }

    })
}