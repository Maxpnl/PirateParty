let icons = document.getElementsByClassName("icon-to-animate");
let svgs = document.getElementsByClassName("svg");

let paragraphs = document.getElementsByClassName("paragraph");
let titles = document.getElementsByClassName("box-title");

// It returns true if the element is in the viewport, false otherwise
var isInViewport = function (elem) {
    var bounding = elem.getBoundingClientRect();
    return (
        bounding.top >= 0 &&
        bounding.left >= 0 &&
        bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
};

// Check if the remaining icons are inside the viewport, if they are, add the animation to both them and the svg
// and then remove the icon-to-animate class from them
window.onscroll = function() {
	for (let i = icons.length - 1; i >= 0; i--) {
		if (isInViewport(icons[i])){
			icons[i].className += " animated rotateIn";
			svgs[i].className.baseVal += " animated heartBeat";

			// Give the white text and the black one different animations
			if (i % 2 == 0) { 
				paragraphs[i].className += " animated slideInLeft";
				titles[i].className += " animated slideInLeft";
			}
			else {
				console.log(paragraphs[i]);
				paragraphs[i].className += " animated slideInRight";
				titles[i].className += " animated slideInLeft";
			}

			icons.className = "box-icon";
		}
	}
};
// Dispatch a scroll event to run the animations on window load
window.onload = function() {
	window.dispatchEvent(new CustomEvent('scroll'));
}