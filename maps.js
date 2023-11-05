const characterMap = new Map([
    ['Main character', 'Spongebob'],
    ['Best friend', 'Patrick'],
    ['Pet', 'Gary'],
    ['Work buddy', 'Squidward'],
    ['Manager', 'Mr. Krabs'],
    ['Teacher', 'Mrs. Puff'],
    ['Location', 'Bikini Bottom']
  ]);

for (const [key, value] of characterMap) {
    console.log(`${key}: ${value}`);
}
console.log(Array.from(characterMap.keys()));
console.log(characterMap.get("Location"));
console.log("Map size: " + characterMap.size);
characterMap.delete("Location");
console.log("Map size: " + characterMap.size);
for (const [key, value] of characterMap) {
    console.log(`${key}: ${value}`);
}
console.log(characterMap.has("Location"))