const main = document.querySelector('main');

function createHeading(color, text){
    const heading = document.createElement('h1');
    heading.setAttribute('style', 'color: ' + color);
    heading.textContent = text;
    return heading;
}

function headingFactory(color) {
//A higher-order function that creates a function for generating headings with the specified color
    return function (text) {
        //A closure function, which has access to to color parameter
      const heading = createHeading(color, text);
      main.appendChild(heading);
    };
}
  
const createRedHeading = headingFactory('red');
const createBlueHeading = headingFactory('blue');

createRedHeading('using factory 1');
createBlueHeading('using factory 2');
