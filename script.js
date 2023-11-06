const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'white'},
        { color: 'white'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
        { color: 'green'},
        { color: 'green'},
    ],
    [
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'pink'},
        { color: 'blue'},
        { color: 'green'},
    ]
];

// Helper functions
function identifySpecies(jellyfish) {
    switch (jellyfish.color) {
        case 'pink':
            return 'pink spotted';
        case 'blue':
            return 'blue stinger';
        case 'green':
            return 'green itches';
        default:
            return 'common';
    }
}

// Score keeping callback function
let totalScore = 0;

function addPoints(species) {
    //Use 1 as default if it's a common jellyfish (any color other than blue, green, or pink)
    const points = speciesPoints[species] || 1;
    totalScore += points;
    console.log(`Total score: ${totalScore}`)
}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish) {
    const species = identifySpecies(jellyfish);
    console.log(`Patrick identified this jellyfish as a ${species} jellyfish`)
    addPoints(species);
}

// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    console.log(`Spongebob caught a ${jellyfish.color} jellyfish`);
    identifyJellyfishAndAddPoints(jellyfish);
}

//The Adventure Starts Here!
for (const day of jellyfishDays) {
    //Reset the score for each day
    totalScore = 0;
    for (const jellyfish of day) {
        catchJellyfish(jellyfish, identifyJellyfishAndAddPoints);
    }
    console.log(`Final score for today: ${totalScore}`);
}