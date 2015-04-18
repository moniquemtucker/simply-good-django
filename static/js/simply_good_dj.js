/**
 * Created by student on 10/30/14.
 */
    $(window).load(function(){
        $('#register-modal').modal('show');
    });

    $(window).load(function(){
        $('#login-modal').modal('show');
    });

$(document).ready(function() {
//    $('#pagepiling').pagepiling();

    $('#pagepiling').pagepiling({
    sectionsColor: ['#f2f2f2', '#00853E', '#EF4B26'],
    navigation: {
    'textColor': '#FFF',
    'bulletsColor': '#FFF',
    'position': 'right',
    'tooltips': ['login/sign up', 'principles', 'goals']
}
});
});
