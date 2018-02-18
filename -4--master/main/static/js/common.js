$(document).ready(function () {

    $(".login_link").click(function(){
    	$(".opacity").fadeIn(500);
    	$(".login_form").fadeIn(500);
    	$(".close_login").fadeIn(500);
    	$(".login_list_1").fadeIn(600);
    	$(".login_list_2").fadeIn(550);
    });

    $(".close_login").click(function(){
    	$(".opacity").fadeOut(300);
    	$(".login_form").fadeOut(300);
    	$(".close_login").fadeOut(300);
    	$(".login_list_1").fadeOut(200);
    	$(".login_list_2").fadeOut(250);
    });

});