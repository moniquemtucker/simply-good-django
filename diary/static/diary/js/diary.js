/**
 * Created by student on 11/8/14.
 */


$(document).ready(function() {
    //ajax to add portion
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    //ajax request for date information
    function addDate(date, userId) {
        $.ajax({
            method: "GET",
            url: "/diary/get_date/",
            data: {"date": date, "userId": userId},
            success: function (res) {
                //if date is not equal to today, get rest of data and update DOM
            console.log(res); // log the returned json to the console
                   $(".wf-portion").remove();
                   $(".pf-portion").remove();
                   $('textarea#notes').val("");
                   for (i = 0; i < res.whole_foods; i++) {
                        $("#diary-wf").append("<li class='wf-portion'>" +
                            "<span class='ionicons ion-ios7-tennisball-outline'></span></li>");
                    }
                   for (i = 0; i < res.processed_foods; i++) {
                        $("#diary-pf").append("<li class='pf-portion'>" +
                            "<span class='ionicons ion-ios7-tennisball-outline'></span></li>");
                    }
                   $("textarea#notes").val(res.notes);

                }

        })
    }

    // ajax request for posting diary info
    function postItems(date, wf_total, pf_total, notes_total) {
        $.ajax({
            "method": "POST",
            "url": "/diary/post_items/",
            "data": {"date":date, "wf_total":wf_total, "pf_total":pf_total, "notes_total": notes_total},
            "success": function (res) {

            }
        });
    }

    //TO DO: add a Python Counter() and an if statement to format; pop ups for goals achieved

    //capture number of portion elements

    (function(){

        function portionCount() {
            var date = dateGroom();
            var wf_total = document.getElementsByClassName('wf-portion').length;
            var pf_total = document.getElementsByClassName('pf-portion').length;
            var notes_total = document.getElementById("notes").value;
            return postItems(date, wf_total, pf_total, notes_total);
        }

        $(".add-portion-wf").click(function () {
        //TO DO: send ajax POST, callback will append the li to the ul parent element
            $("#diary-wf").append("<li class='wf-portion'>" +
                "<span class='ionicons ion-ios7-tennisball-outline'></span></li>");
            portionCount();
        });

        $(".remove-portion-wf").click(function () {
        //TO DO: send ajax POST, callback will append the li to the ul parent element
            $(".wf-portion").last().remove();
            portionCount();
        });

        $(".add-portion-pf").click(function () {
            $("#diary-pf").append("<li class='pf-portion'>" +
                "<span class='ionicons ion-ios7-tennisball-outline'></span></li>");
            portionCount();

        });

        $(".remove-portion-pf").click(function () {
            $(".pf-portion").last().remove();
            portionCount();
        });

        $( "#notes" ).change(function() {
            var date = dateGroom();
            var wf_total = document.getElementsByClassName('wf-portion').length;
            var pf_total = document.getElementsByClassName('pf-portion').length;
            var notes_total = document.getElementById("notes").value;
            return postItems(date, wf_total, pf_total, notes_total);
        });
    })();

    //extract user pk from current url
    function getUserId () {
        var url = window.location,
        splitUrl = url.toString().split("/");
        return splitUrl[4];
    }

    //capture date information and turn into ISO format
    function dateGroom() {
        var active_date = document.getElementById('date-cal').innerHTML;
        var active_year = document.getElementById('year-cal').innerHTML;
        var active_date_array = active_date.split(" ");
        var active_month = active_date_array[0];
        if (active_date_array[1].length > 3) {
            var active_day = active_date_array[1].substring(0, 2);
        }
        else {
            var active_day = "0" + active_date_array[1].substring(0, 1);
        }
        var monthmatch = {
            January: "01",
            February: "02",
            March: "03",
            April: "04",
            May: "05",
            June: "06",
            July: "07",
            August: "08",
            September: "09",
            October: "10",
            November: "11",
            December: "12"
        };

        var monthnum = monthmatch[active_month];
        // TO DO --- determine if date needs to be a particular data type
        return active_year + "-" + monthnum + "-" + active_day
    }

    // test calendar
    $('.date-picker').each(function () {
        var $datepicker = $(this),
            cur_date = ($datepicker.data('date') ? moment($datepicker.data('date'), "YYYY/MM/DD") : moment()),
            format = {
                "weekday": ($datepicker.find('.weekday').data('format') ? $datepicker.find('.weekday').data('format') : "dddd"),
                "date": ($datepicker.find('.date').data('format') ? $datepicker.find('.date').data('format') : "MMMM Do"),
                "year": ($datepicker.find('.year').data('year') ? $datepicker.find('.weekday').data('format') : "YYYY")
            };

        function updateDisplay(cur_date) {
            $datepicker.find('.date-container > .weekday').text(cur_date.format(format.weekday));
            $datepicker.find('.date-container > .date').text(cur_date.format(format.date));
            $datepicker.find('.date-container > .year').text(cur_date.format(format.year));
            $datepicker.data('date', cur_date.format('YYYY/MM/DD'));
            $datepicker.find('.input-datepicker').removeClass('show-input');
        }

        updateDisplay(cur_date);

        $datepicker.on('click', '[data-toggle="calendar"]', function (event) {
            event.preventDefault();
            $datepicker.find('.input-datepicker').toggleClass('show-input');
        });

        $datepicker.on('click', '.input-datepicker > .input-group-btn > button', function (event) {
            event.preventDefault();
            var $input = $(this).closest('.input-datepicker').find('input'),
                date_format = ($input.data('format') ? $input.data('format') : "YYYY/MM/DD");
            if (moment($input.val(), date_format).isValid()) {
                updateDisplay(moment($input.val(), date_format));
                // event handler for changing date and ajax request
                var date = dateGroom();
                var userId = getUserId();
                return addDate(date, userId);
            } else {
                alert('Invalid Date');
            }
        });

        $datepicker.on('click', '[data-toggle="datepicker"]', function (event) {
            event.preventDefault();

            var cur_date = moment($(this).closest('.date-picker').data('date'), "YYYY/MM/DD"),
                date_type = ($datepicker.data('type') ? $datepicker.data('type') : "days"),
                type = ($(this).data('type') ? $(this).data('type') : "add"),
                amt = ($(this).data('amt') ? $(this).data('amt') : 1);

            if (type == "add") {
                cur_date = cur_date.add(date_type, amt);
            } else if (type == "subtract") {
                cur_date = cur_date.subtract(date_type, amt);
            }
            // event handler for changing date and ajax request
            updateDisplay(cur_date);
            var date = dateGroom();
            var userId = getUserId();
            return addDate(date, userId);
        });

        // TO DO: remove code
        if ($datepicker.data('keyboard') == true) {
            $(window).on('keydown', function (event) {
                if (event.which == 37) {
                    $datepicker.find('span:eq(0)').trigger('click');
                } else if (event.which == 39) {
                    $datepicker.find('span:eq(1)').trigger('click');
                }
            });
        }
    });

    // for trends
    $(function () {
        $('#chart-container').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: 'Diary Week in Review'
            },
            xAxis: {
                categories: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Total food consumption'
                },
                stackLabels: {
                    enabled: true,
                    style: {
                        fontWeight: 'bold',
                        color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
                    }
                }
            },
            legend: {
                align: 'right',
                x: -70,
                verticalAlign: 'top',
                y: 20,
                floating: true,
                backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
                borderColor: '#CCC',
                borderWidth: 1,
                shadow: false
            },
            tooltip: {
                formatter: function () {
                    return '<b>' + this.x + '</b><br/>' +
                        this.series.name + ': ' + this.y + '<br/>' +
                        'Total: ' + this.point.stackTotal;
                }
            },
            plotOptions: {
                column: {
                    stacking: 'normal',
                    dataLabels: {
                        enabled: true,
                        color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                        style: {
                            textShadow: '0 0 3px black, 0 0 3px black'
                        }
                    }
                }
            },
            series: [ {
                name: 'Whole Foods',
                data: [2, 2, 3, 2, 1]
            }, {
                name: 'Processed Foods',
                data: [3, 4, 4, 2, 5]
            }]
        });
    })
;});

