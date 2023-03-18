/* eslint-disable template-curly-spacing */
/* eslint-disable array-bracket-spacing */
/* eslint-disable space-in-parens */
// For more information, see greensock.com/docs/v3/Plugins/ScrollTrigger
window.gsap.registerPlugin(window.ScrollTrigger);
window.gsap.registerPlugin(window.SplitText);

// Animation for homepage product cards
if (window.innerWidth > 990 && window.location.pathname === '/') {
	const defaultPositon = {
		x: 0,
		y: 0,
		scale: 1,
		rotate: 0,
	};

	window.gsap
		.timeline({
			scrollTrigger: {
				trigger: '.fisdom-services-main',
				start: '0% 20%',
				end: '+=600px 15%',
				scrub: 0.6,
				// markers: true,
			},
		})
		.fromTo(
			'.service-1',
			{
				...defaultPositon,
			},
			{
				x: 400,
				y: 600,
				scale: 0.3,
				rotate: -10,
				ease: 'power2.out',
				delay: 0.1,
			},
			'start',
		)
		.fromTo(
			'.service-2',
			{
				...defaultPositon,
			},
			{
				x: 150,
				y: 600,
				scale: 0.3,
				rotate: 0,
				ease: 'power2.out',
				delay: 0.3,
			},
			'start',
		)
		.fromTo(
			'.service-3',
			{
				...defaultPositon,
			},
			{
				x: -150,
				y: 600,
				scale: 0.3,
				rotate: 0,
				ease: 'power2.out',
				delay: 0.2,
			},
			'start',
		)
		.fromTo(
			'.service-4',
			{
				...defaultPositon,
			},
			{
				x: -400,
				y: 600,
				scale: 0.3,
				rotate: 0,
				ease: 'power2.out',
				delay: 0.38,
			},
			'start',
		);

	// Animation for homepage phone screen

	window.gsap
		.timeline({
			scrollTrigger: {
				trigger: '.app-feature-1',
				start: '0% 30%',
				end: '60% 15%',
				scrub: 0.6,
				// markers: true,
			},
		})
		.to('.phone-asset-1', {
			x: 100,
			rotation: 0,
			autoAlpha: 0,
		});

	window.gsap
		.timeline({
			scrollTrigger: {
				trigger: '.app-feature-2',
				start: '-40% 30%',
				end: '60% 15%',
				scrub: 0.6,
				// markers: true,
			},
		})
		.to(
			'.screen-2',
			{
				opacity: 1,
			},
			'start',
		)
		.fromTo(
			'.phone-asset-2',
			{
				xPercent: -40,
				rotation: 0,
				opacity: 0,
			},
			{
				xPercent: 0,
				rotation: 20,
				opacity: 1,
			},
			'start',
		)
		.to('.phone-asset-2', {
			xPercent: -40,
			rotation: 0,
			opacity: 0,
			delay: 0.4,
		});

	window.gsap
		.timeline({
			scrollTrigger: {
				trigger: '.app-feature-3',
				start: '-40% 30%',
				end: '0% 15%',
				scrub: 0.6,
				// markers: true,
			},
		})
		.to(
			'.screen-3',
			{
				opacity: 1,
			},
			'start',
		)

		.from(
			'.phone-asset-3',
			{
				xPercent: 40,
				rotation: 0,
				autoAlpha: 0,
				ease: 'power2.out',
			},
			'start',
		);
}

if (window.location.pathname === '/career/') {
	window.gsap
		.timeline({
			scrollTrigger: {
				trigger: '.career-hero',
				start: '0% 0%',
				end: '100% 0%',
				scrub: 0.8,
				// markers: true,
			},
		})

		.to(
			'.career-hero-slider',
			{
				xPercent: -30,
				yPercent: 20,
				ease: 'power2.out',
			},
			'start',
		);

	window.gsap.set('.single-career-gallery', { yPercent: 100, autoAlpha: 0 });

	window.ScrollTrigger.batch('.single-career-gallery', {
		scrub: 0.5,
		trigger: '.career-gallery',
		start: '0% 100%',
		end: '20% 30%',
		// markers: true,
		onEnter: (elements) => {
			window.gsap.to(elements, {
				yPercent: 0,
				autoAlpha: 1,
				stagger: 0.01,
				scrollTrigger: {},
			});
		},
	});

	if (window.innerWidth > 990) {
		window.gsap
			.timeline({
				scrollTrigger: {
					trigger: '.jobs-gallery',
					start: '0% 50%%',
					end: '100% 30%',
					scrub: 0.8,
					// markers: true,
				},
			})
			.to(
				'.job-gallery-col',
				{
					y: '60px',
					ease: 'power2.out',
				},
				'start',
			)
			.to(
				'.job-gallery-col-2',
				{
					y: '-60px',
					ease: 'power2.out',
				},
				'start',
			);
	}
}

if (window.location.pathname.match(/wealth/)) {
	const splitText = new window.SplitText('#wealth-hero-heading', {
		type: 'lines',
	});
	const tl = window.gsap.timeline();
	const zoomImageOnScroll = [
		window.gsap.utils.toArray('.zoom-image-on-scroll-1'),
		window.gsap.utils.toArray('.zoom-image-on-scroll-2'),
		window.gsap.utils.toArray('.zoom-image-on-scroll-3'),
		window.gsap.utils.toArray('.zoom-image-on-scroll-4'),
	];
	const appearOnScroll = window.gsap.utils.toArray('.appear-on-scroll');
	const parallaxBackground = window.gsap.utils.toArray('.parallax-background');
	const targets = [
		...splitText.lines,
		...window.gsap.utils.toArray('#wealth-hero-content > div'),
	];

	tl.from(targets, {
		duration: 2,
		delay: 0.1,
		opacity: 0,
		y: 150,
		ease: 'power2.out',
		stagger: 0.2,
	});

	zoomImageOnScroll.forEach((group) => {
		group.forEach((image, index) => {
			window.gsap.from(image, {
				delay: 0.1 * index,
				duration: 2,
				scale: 1.3,
				ease: 'power2.out',
				scrollTrigger: {
					trigger: image,
					start: 'top bottom',
				},
			});
		});
	});

	appearOnScroll.forEach((trigger, index) => {
		window.gsap.from(trigger, {
			delay: 0.05 * index,
			duration: 2,
			opacity: 0,
			y: 150,
			ease: 'power2.out',
			scrollTrigger: {
				trigger,
				start: 'top bottom',
			},
		});
	});

	const getRatio = (el) =>
		window.innerHeight / (window.innerHeight + el.offsetHeight);

	parallaxBackground.forEach((section) => {
		if (window.innerWidth > 767) {
			window.gsap.fromTo(
				section,
				{
					backgroundPosition: () =>
						`50% ${-window.innerHeight * getRatio(section)}px`,
				},
				{
					backgroundPosition: () =>
						`50% ${window.innerHeight * (1 - getRatio(section))}px`,
					ease: 'none',
					scrollTrigger: {
						trigger: section,
						start: 'top bottom',
						end: 'bottom top',
						scrub: true,
						invalidateOnRefresh: true, // to make it responsive
					},
				},
			);
		} else {
			window.gsap.fromTo(
				section,
				{
					backgroundPosition: () => `50% 50px`,
				},
				{
					backgroundPosition: () => `50% -200px`,
					ease: 'none',
					scrollTrigger: {
						trigger: section,
						start: 'top bottom',
						end: 'bottom top',
						scrub: 0.6,
						invalidateOnRefresh: true, // to make it responsive
					},
				},
			);
		}
	});

	const fourCs = document.getElementById('four-cs');

	window.gsap.to('#four-cs > div', {
		x: `-${fourCs.scrollWidth - fourCs.offsetWidth}px`,
		ease: 'none',
		duration: 3,
		scrollTrigger: {
			trigger: '#solutions-cs-container',
			start: 'bottom bottom',
			end: '+=1000',
			scrub: 0.9,
			pin: true,
		},
	});

	const smartTrigger = {
		trigger: '#wealth-smart',
		start: 'top 80%',
		end: '170% 60%',
		scrub: 0.6,
		// markers: true,
	};
	const smartTrigger2 = {
		trigger: '#wealth-smart',
		start: '150px 80%',
		end: '170% 60%',
		scrub: 0.6,
		// markers: true,
	};

	window.gsap.fromTo(
		'#wealth-smart-center-circle',
		{
			rotation: 0,
		},
		{ rotation: 40, scrollTrigger: smartTrigger },
	);
	window.gsap.fromTo(
		'.wealth-smart-side-1',
		{ y: 0 },
		{ y: -300, scrollTrigger: smartTrigger2 },
	);
	window.gsap.fromTo(
		'.wealth-smart-side-2',
		{ y: 0 },
		{ y: -100, scrollTrigger: smartTrigger2 },
	);
	window.gsap.fromTo(
		'.wealth-smart-side-3',
		{ y: -80 },
		{ y: 20, scrollTrigger: smartTrigger2 },
	);
}
