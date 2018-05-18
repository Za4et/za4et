function permisiion_journal(href) {
    if (href === '#') {
        $('.journ_frame').hide();
        $('.journ_select_text').html('');
        $('.journ_select_text').html('<div class="journ_err_select_text">\n' +
            '<p>Выберите журнал группы,</p>\n' +
            '<p>в которой состоите!</p>\n' +
            '</div>')
    }
    else $('.journ_frame').css('display', 'block')

}

function recaptchaCallback() {

        $('.sign_sub').css('opacity', '1');
        $('.sign_sub').attr('type', 'submit')

};