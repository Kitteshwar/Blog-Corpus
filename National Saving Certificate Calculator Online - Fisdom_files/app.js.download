/* eslint-disable array-bracket-spacing */
/* eslint-disable computed-property-spacing */
/* eslint-disable camelcase */
/* eslint-disable template-curly-spacing */
/* eslint-disable space-in-parens */
const hamburger = document.querySelector('.hamburger');
const mainNav = document.querySelector('.menu-main');

const toggleNav = () => {
	mainNav.classList.toggle('open');
};

hamburger.addEventListener('click', toggleNav);

const dropdown = document.querySelectorAll('.dropdown');

Array.from(dropdown).forEach((drop) => {
	drop.addEventListener('click', () => {
		dropdown.forEach((d) => {
			if (d !== drop) {
				d.classList.remove('open');
			}
		});
		drop.classList.toggle('open');
	});
});

// hide header on scroll

// grab an element
const header = document.querySelector('.header-main');
// construct an instance of Headroom, passing the element
const headroom = new Headroom(header);
// initialise
headroom.init();

// $(document).ready(function () {
// 	$('.readmore-btn').click(function () {
// 		$(this).parent().children('.hidden-text').slideToggle();
// 		if ($(this).text() === 'Read less') {
// 			$(this).text('Read more...');
// 		} else {
// 			$(this).text('Read less');
// 		}
// 	});
// });

const buttonParallax = document.querySelectorAll('.anim-button');

if (window.innerWidth > 1200) {
	Array.from(buttonParallax).forEach((item) => {
		item.addEventListener('mousemove', (e) => {
			// const position = item.getAttribute('value');
			const rect = e.target.getBoundingClientRect();
			const x = (e.clientX - rect.left) / 20; //x position within the element.
			const y = (e.clientY - rect.top) / 100; //y position within the element.

			item.style.transform = `translate3d(${x}%, ${x}%, 0) skew(0, ${y}deg) scale(1.1)`;
		});

		item.addEventListener('mouseleave', () => {
			item.style.transform = `translateX(0px) skew(0, 0deg) scale(1)`;
		});
	});
}

const dataAnimContainer = document.querySelectorAll('[data-anim-container]');

dataAnimContainer.forEach((container) => {
	document.addEventListener(
		'DOMContentLoaded',
		() => {
			const lis = Array.prototype.slice.call(
				container.querySelectorAll('.anim-common'),
			);
			if (lis) {
				const lis_count = lis.length;
				let active_li_index = 0;

				setInterval(() => {
					const active_li = container.querySelector('.anim-common.active');

					if (lis.indexOf(active_li) === lis_count - 1) {
						active_li_index = 0;
					} else {
						active_li_index++;
					}

					active_li.classList.remove('active');
					container
						.querySelectorAll('.anim-common')
						[active_li_index].classList.add('active');
				}, 4000);
			}
		},
		false,
	);
});

// document.addEventListener(
// 	'DOMContentLoaded',
// 	function () {
// 		if (lis) {
// 			var lis = Array.prototype.slice.call(
// 				document.querySelectorAll('.single-bottom-img-content'),
// 			);
// 			const lis_count = lis.length;
// 			let active_li_index = 0;

// 			setInterval(function () {
// 				const active_li = document.querySelector(
// 					'.single-bottom-img-content.active',
// 				);

// 				if (lis.indexOf(active_li) == lis_count - 1) {
// 					active_li_index = 0;
// 				} else {
// 					active_li_index++;
// 				}

// 				active_li.classList.remove('active');
// 				document
// 					.querySelectorAll('.single-bottom-img-content')
// 					[active_li_index].classList.add('active');
// 			}, 4000);
// 		}
// 	},
// 	false,
// );

window.addEventListener('load', () => {
	const dataTabContainer = document.querySelectorAll('[data-tab-container]');

	dataTabContainer.forEach((container) => {
		const theTabs = container.querySelectorAll('.nav-tabs button');

		function theTabClicks(tabClickEvent) {
			const clickedTab = tabClickEvent.currentTarget;

			// var tabParent =
			// 	tabClickEvent.currentTarget.parentNode.parentNode.parentNode.parentNode;
			// console.log(tabParent);
			// var theTabs = tabParent.querySelectorAll('.nav-tabs button');
			for (let i = 0; i < theTabs.length; i++) {
				theTabs[i].classList.remove('active');
			}

			clickedTab.classList.add('active');
			tabClickEvent.preventDefault();

			const contentPanes = container.querySelectorAll('.tab-pane');

			for (let i = 0; i < contentPanes.length; i++) {
				contentPanes[i].classList.remove('active');
			}

			const anchorReference = tabClickEvent.target;

			const activePaneId = anchorReference.getAttribute('data-tab');
			const activePane = container.querySelectorAll('.' + activePaneId);

			Array.from(activePane).forEach((item) => {
				item.classList.add('active');
			});
		}
		for (let i = 0; i < theTabs.length; i++) {
			theTabs[i].addEventListener('click', theTabClicks);
		}
	});
	// store tabs variable
});

const readmoreTrigger = document.querySelector('.readmore-trigger');
const readmoretext = document.querySelector('.readmore-text');

if (readmoreTrigger) {
	readmoreTrigger.addEventListener('click', () => {
		readmoretext.classList.toggle('active');

		if (readmoreTrigger.innerHTML === 'Read less...') {
			readmoreTrigger.innerHTML = 'Read more...';
		} else {
			readmoreTrigger.innerHTML = 'Read less...';
		}
	});
}
const scrollContents = document.querySelectorAll('.scroll-item-content');
const scrollImages = document.querySelectorAll('.scroll-img ');

function handleIntersection(entries) {
	entries.map((entry) => {
		if (entry.isIntersecting) {
			[scrollContents, scrollImages].forEach((e) =>
				e.forEach((el) => el.classList.remove('active')),
			);
			[scrollImages].forEach((scrollArr) =>
				scrollArr.forEach((scrollItem) =>
					scrollItem.dataset?.id === entry.target.dataset?.id
						? scrollItem.classList.add('active')
						: '',
				),
			);
			[scrollContents].forEach((scrollArr) =>
				scrollArr.forEach((scrollItem) =>
					scrollItem.dataset?.id === entry.target.dataset?.id
						? scrollItem.classList.add('active')
						: '',
				),
			);
		}
		return entry;
	});
}

const observer = new IntersectionObserver(handleIntersection, {
	threshold: 0.5,
	rootMargin: '-100px',
});

scrollContents.forEach((scrollcontent) => observer.observe(scrollcontent));

// add absolute header to certain page

function headerHeight() {
	const headerMain = document.querySelector('.header-main');
	const headerCompensate = document.querySelector('.header-height');

	const Headerheight = headerMain.offsetHeight;
	if (headerCompensate) {
		headerCompensate.style.height = `${Headerheight}px`;
	}
}

const section = document.querySelector('section');

if (section) {
	if (section.classList.contains('abs-header')) {
		document.querySelector('.header-main').classList.add('abs-header');
	}
}

const absHeader = document.getElementsByClassName('abs-header').length > 0;

if (absHeader === false) {
	headerHeight();
}

const activeclass = document.querySelectorAll('.single-employee-testimonial');

activeclass.forEach((i) => {
	i.addEventListener('click', (e) => {
		document
			.querySelector('.single-employee-testimonial.active')
			.classList.remove('active');
		e.target.closest('.single-employee-testimonial').classList.add('active');
	});
});

// add class on header on scroll

let scrollpos = window.scrollY;
const navHeader = document.querySelector('.header-main');
const header_height = window.location.pathname.match(/private-wealth/)
	? 1
	: navHeader.offsetHeight;

const addClassOnScroll = () => navHeader.classList.add('scrolled');
const removeClassOnScroll = () => navHeader.classList.remove('scrolled');

window.addEventListener('scroll', () => {
	scrollpos = window.scrollY;

	if (scrollpos >= header_height) {
		addClassOnScroll();
	} else {
		removeClassOnScroll();
	}
});

const arrowLeft =
	'<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="m15 18-6-6 6-6" stroke="#0F0F0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';

const arrowRight =
	'<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="m9 18 6-6-6-6" stroke="#0F0F0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';

const marqueesliderCommon = {
	autoplay: true,
	preventActionWhenRunning: true,
	autoplayTimeout: 0,
	autoplayButtonOutput: false,
	mouseDrag: false,
	loop: true,
	speed: 4000,
	nav: false,
	controls: false,
	navPosition: 'bottom',
};

const trustedBanksSlider = document.querySelector('.bank-slider-1');

if (trustedBanksSlider) {
	window.tns({
		container: trustedBanksSlider,
		autoplayDirection: 'backward',
		...marqueesliderCommon,

		responsive: {
			0: {
				gutter: 15,
				items: 1.5,
			},

			768: {
				gutter: 32,
				items: 3,
			},

			1200: {
				items: 4,
			},
		},
	});
}
const trustedBanksSliderTwo = document.querySelector('.bank-slider-2');

if (trustedBanksSliderTwo) {
	window.tns({
		container: trustedBanksSliderTwo,
		...marqueesliderCommon,

		responsive: {
			0: {
				gutter: 15,
				items: 1.5,
			},

			768: {
				gutter: 32,
				items: 3,
			},

			1200: {
				items: 4,
			},
		},
	});
}
const careerTextMarquee = document.querySelector('.career-text-slider');

if (careerTextMarquee) {
	window.tns({
		container: careerTextMarquee,
		...marqueesliderCommon,

		responsive: {
			0: {
				gutter: 15,
				items: 1.5,
			},

			768: {
				gutter: 32,
				items: 3,
			},

			1200: {
				items: 5,
			},
		},
	});
}
const careerGallerySlider = document.querySelector('.career-gallery-slider');

if (careerGallerySlider) {
	window.tns({
		container: careerGallerySlider,
		autoWidth: true,
		...marqueesliderCommon,

		responsive: {
			0: {
				gutter: 15,
				items: 1.5,
			},

			768: {
				gutter: 32,
				items: 3,
			},

			1200: {
				items: 6,
			},
		},
	});
}

const awardSlider = document.querySelector('.award-slider-main');

if (awardSlider) {
	window.tns({
		container: awardSlider,
		autoplay: true,
		autoplayTimeout: 10000,
		autoplayButtonOutput: false,
		mouseDrag: false,
		loop: true,
		speed: 800,
		nav: false,
		controls: true,
		navPosition: 'bottom',
		controlsContainer: '.award-controls',
		mode: 'gallery',

		responsive: {
			0: {
				gutter: 0,
				items: 1,
			},
		},
	});
}

const testimonialSlider = document.querySelector('.testimonial-slider');

if (testimonialSlider) {
	window.tns({
		container: testimonialSlider,
		autoplay: true,
		autoplayButtonOutput: false,
		mouseDrag: false,
		loop: true,
		speed: 800,
		controls: true,
		navPosition: 'bottom',
		controlsContainer: '.testimonial-controls',

		responsive: {
			0: {
				gutter: 15,
				items: 1,
			},

			768: {
				gutter: 32,
				items: 3,
			},

			1200: {
				items: 3,
			},
		},
	});
}

const blogCategoryFilter = document.querySelector('.blog-category-filter');

if (blogCategoryFilter) {
	window.tns({
		container: blogCategoryFilter,
		autoplay: false,
		autoplayButtonOutput: false,
		mouseDrag: false,
		loop: false,
		speed: 800,
		nav: false,
		controls: true,
		controlsText: [arrowLeft, arrowRight],
		autoWidth: true,

		responsive: {
			0: {
				// gutter: 15,
				items: 3,
			},

			768: {
				// gutter: 32,
				items: 3.2,
			},

			1200: {
				items: 10,
			},
		},
	});
}

const popularArcticleSlider = document.querySelector('.popular-article-slider');

if (popularArcticleSlider) {
	window.tns({
		container: popularArcticleSlider,
		autoplay: false,
		autoplayButtonOutput: false,
		mouseDrag: false,
		loop: false,
		speed: 800,
		nav: false,
		controls: true,
		controlsText: [arrowLeft, arrowRight],

		responsive: {
			0: {
				gutter: 15,
				items: 1,
			},

			768: {
				gutter: 32,
				items: 3,
			},

			1200: {
				items: 2.3,
			},
		},
	});
}

const relatedBlogSlider = document.querySelector('.related-article-slider');

if (relatedBlogSlider) {
	window.tns({
		container: relatedBlogSlider,
		autoplay: false,
		autoplayButtonOutput: false,
		mouseDrag: false,
		loop: true,
		speed: 800,
		nav: false,
		controls: true,
		controlsText: [arrowLeft, arrowRight],

		responsive: {
			0: {
				gutter: 15,
				items: 1,
			},

			768: {
				gutter: 32,
				items: 3,
			},

			1200: {
				items: 3,
			},
		},
	});
}
const whoWeareSlider = document.querySelector('.who-we-are-slider');

if (whoWeareSlider) {
	window.tns({
		container: whoWeareSlider,
		autoplay: false,
		autoplayButtonOutput: false,
		mouseDrag: false,
		loop: true,
		speed: 800,
		nav: false,
		controls: true,
		controlsPosition: 'bottom',
		controlsText: [arrowLeft, arrowRight],

		responsive: {
			0: {
				gutter: 15,
				items: 1.2,
			},

			768: {
				gutter: 30,
				items: 3,
			},

			1200: {
				items: 4,
			},
		},
	});
}

const logoSlider = document.querySelector('.featured-logo-slider');

if (logoSlider) {
	window.tns({
		container: logoSlider,
		autoplayButtonOutput: false,
		mouseDrag: false,
		speed: 800,
		nav: false,
		controls: false,
		controlsText: [arrowLeft, arrowRight],

		responsive: {
			0: {
				gutter: 15,
				items: 2,
				loop: true,
				autoplay: true,
				autoplayTimeout: 0,
				preventActionWhenRunning: true,
				speed: 2000,
			},

			768: {
				gutter: 32,
				items: 3,
				autoplay: false,
				loop: false,
			},

			1200: {
				disable: true,
			},
		},
	});
}

const careerEmployeeTestimonialSlider = document.querySelector(
	'.employee-testimonial-slider',
);

if (careerEmployeeTestimonialSlider) {
	window.tns({
		container: careerEmployeeTestimonialSlider,
		autoplay: false,
		autoplayButtonOutput: false,
		mouseDrag: false,
		loop: false,
		speed: 800,
		nav: false,
		controls: true,
		controlsPosition: 'bottom',
		controlsText: [arrowLeft, arrowRight],

		responsive: {
			0: {
				gutter: 15,
				items: 1,
			},

			768: {
				gutter: 30,
				items: 2,
			},

			1200: {
				disable: true,
			},
		},
	});
}

const wealthWordSlider = document.querySelector('#ceo-word');

if (wealthWordSlider) {
	window.tns({
		...marqueesliderCommon,
		container: wealthWordSlider,
		speed: 8000,
		autoWidth: true,
	});
}

// NoUI Range slider

const rangeSlider = document.getElementById('slider-range');

if (rangeSlider) {
	window.noUiSlider.create(rangeSlider, {
		start: [4000],
		connect: 'lower',
		range: {
			min: [2000],
			max: [10000],
		},
	});
}

const rangeSlider2 = document.getElementById('slider-range2');
if (rangeSlider2) {
	window.noUiSlider.create(rangeSlider2, {
		start: [4000],
		connect: 'lower',
		range: {
			min: [2000],
			max: [10000],
		},
	});
}

const valuesSlider = document.getElementById('slider-range3');

if (valuesSlider) {
	const valuesForSlider = ['5Y', '10Y', '20Y', '30Y', '40Y', '50Y']; // 16 values

	const format = {
		to(value) {
			return valuesForSlider[Math.round(value)];
		},
		from(value) {
			return valuesForSlider.indexOf(Number(value));
		},
	};

	window.noUiSlider.create(valuesSlider, {
		start: [1],
		// A linear range from 0 to 15 (16 values)
		range: { min: 0, max: valuesForSlider.length - 1 },
		// steps of 1
		connect: 'lower',
		step: 1,
		format,
		pips: { mode: 'steps', format, density: 50 },
	});

	// The display values can be used to control the slider
	valuesSlider.noUiSlider.set(['1']);
}

const shareButton = document.querySelector('[data-share-btn]');
if (shareButton) {
	const shareToggle = shareButton.querySelector('button');

	if (shareToggle) {
		shareToggle.addEventListener('click', () => {
			if (shareButton === null) {
				return;
			}
			if (shareButton.classList.contains('active-list')) {
				shareButton.classList.remove('active-list');
			} else {
				shareButton.classList.add('active-list');
			}
		});
	}
}

const wealthOptionsExpandable = document.querySelectorAll(
	'.wealth-options-expandable-trigger',
);

if (wealthOptionsExpandable.length > 0) {
	const wealthOptionsExpandableSections = document.querySelector(
		'.wealth-options-expandable-sections',
	).children;

	const clickHandler = (e) => {
		const clickID = Number(
			e.target.closest('.wealth-options-expandable-trigger').dataset.id,
		);
		Array.from(wealthOptionsExpandableSections).forEach((element, index) => {
			const contentEl = element.children[1];

			if (clickID === index && contentEl.classList.contains('max-h-0')) {
				contentEl.classList.add('max-h-[1000px]');
				contentEl.classList.remove('max-h-0');
			} else {
				contentEl.classList.remove('max-h-[1000px]');
				contentEl.classList.add('max-h-0');
			}
		});
	};

	Array.from(wealthOptionsExpandable).forEach((el) => {
		el.onclick = clickHandler;
	});
}
const researchCategoryFilter = document.querySelector('.js-tabs__header');

if (researchCategoryFilter) {
	window.tns({
		container: researchCategoryFilter,
		autoplay: false,
		autoplayButtonOutput: false,
		mouseDrag: false,
		loop: false,
		speed: 800,
		nav: false,
		controls: true,
		controlsText: [arrowLeft, arrowRight],
		autoWidth: true,
		disable:true,
		responsive: {
			0: {
				// gutter: 15,
				items: 1.5,	
				disable:false,
				gutter: 15,
			},
			1200: {
				disable: true,
			},
			
		},
	});
}