jQuery(function ($) {
	'use strict';

	//Responsive Nav
	$('li.dropdown').find('.fa-angle-down').each(function () {
		$(this).on('click', function () {
			if ($(window).width() < 768) {
				$(this).parent().next().slideToggle();
			}
			return false;
		});
	});

	//Fit Vids
	if ($('#video-container').length) {
		$("#video-container").fitVids();
	}

	//Initiat WOW JS
	new WOW().init();

	// portfolio filter
	$(window).load(function () {

		$('.main-slider').addClass('animate-in');
		$('.preloader').remove();
		//End Preloader

		if ($('.masonery_area').length) {
			$('.masonery_area').masonry(); //Masonry
		}

		var $portfolio_selectors = $('.portfolio-filter >li>a');

		if ($portfolio_selectors.length) {

			var $portfolio = $('.portfolio-items');
			$portfolio.isotope({
				itemSelector: '.portfolio-item',
				layoutMode: 'fitRows'
			});

			$portfolio_selectors.on('click', function () {
				$portfolio_selectors.removeClass('active');
				$(this).addClass('active');
				var selector = $(this).attr('data-filter');
				$portfolio.isotope({
					filter: selector
				});
				return false;
			});
		}
	});

	var myCarouselFirstChild = $('.carousel-inner>.item:first-child')
	myCarouselFirstChild.addClass('active')

	// !!!!
	// var mainMenu=$('#main-menu')
	// mainMenu.click(function(event){
	// 	event.preventDefault()
	// 	console.log(event)
	// })
	// !!!!

	$('.navbar-stacked > li > a, .my-nav-pills > li > a').on('click', function (e) {
		e.preventDefault()

		const href = $(this).attr('href').split('?')
		const hrefQuery = href[1]
		const location = window.location.href.split('?')
		const query = location[1]

		if (hrefQuery) {
			let result = ''
			let hrefQueryParam = hrefQuery.split('=')

			if (query) {
				console.log(query)
				const queryParams = query.split('&')
				
				for (let i = 0; i < queryParams.length-1; i++) {
					const queryParam = queryParams[i].split('=')

					if (queryParam[0] == hrefQueryParam[0]) {
						result += `${hrefQueryParam[0]}=${hrefQueryParam[1]}&`
					}else{
						result += `${queryParam[0]}=${queryParam[1]}&`
						if(queryParams.length-1==1){
							result += `${hrefQueryParam[0]}=${hrefQueryParam[1]}&`
						}
					}
				}
			}else{
				result += `${hrefQueryParam[0]}=${hrefQueryParam[1]}&`
			}
			window.location.replace(`${location[0]}?${result}`)
		} else {
			window.location.replace(`${location[0]}`)
		}
	})

	$('.blog-pagination > .pagination > li > a').on('click',function(e){
		e.preventDefault()
		const hrefArr=$(this).attr('href').split('?')


		const queryParams=window.location.href.split('?')

		let result=''
		result+=hrefArr[1]

		if(queryParams[1]){
			const queryParamsArr=queryParams[1].split('&')

			for(let i=0;i<queryParamsArr.length-1;i++){
				const queryParam=queryParamsArr[i].split('=')

				result+=`${queryParam[0]}=${queryParam[1]}${i<queryParamsArr.length-1?'&':''}`
			}
		}
		window.location.replace(`${queryParams[0]}?${result}`)
	})

	$('.timer').each(count);

	function count(options) {
		var $this = $(this);
		options = $.extend({}, options || {}, $this.data('countToOptions') || {});
		$this.countTo(options);
	}

	// Search
	$('.fa-search').on('click', function () {
		$('.field-toggle').fadeToggle(200);
	});

	// Contact form
	var form = $('#main-contact-form');
	form.submit(function (event) {
		event.preventDefault();
		var form_status = $('<div class="form_status"></div>');

		var data = $(this).serializeArray();
		var $data = {}
		$.each(data, function () {
			$data[this.name] = this.value;
		});

		$.ajax({
			type: $(this).attr('method'),
			url: $(this).attr('action'),
			data: $data,
			beforeSend: function () {
				form.prepend(form_status.html('<p><i class="fa fa-spinner fa-spin"></i> Email is sending...</p>').fadeIn());
			},
			error: function (error) {
				form_status.html(`<p class="text-dangerr">Server Error</p>`);
			}
		}).done(function (data) {
			var name = document.getElementById('id_name')
			var email = document.getElementById('id_email')
			var text = document.getElementById('message')
			name.value = ''
			email.value = ''
			text.value = ''

			form_status.html('<p class="text-success">Thank you for contact us. As early as possible  we will contact you</p>').delay(3000).fadeOut();
		});
	});



	// Progress Bar
	$.each($('div.progress-bar'), function () {
		$(this).css('width', $(this).attr('data-transition') + '%');
	});

	if ($('#gmap').length) {
		var map;

		map = new GMaps({
			el: '#gmap',
			lat: 43.04446,
			lng: -76.130791,
			scrollwheel: false,
			zoom: 16,
			zoomControl: false,
			panControl: false,
			streetViewControl: false,
			mapTypeControl: false,
			overviewMapControl: false,
			clickable: false
		});

		map.addMarker({
			lat: 43.04446,
			lng: -76.130791,
			animation: google.maps.Animation.DROP,
			verticalAlign: 'bottom',
			horizontalAlign: 'center',
			backgroundColor: '#3e8bff',
		});
	}
});