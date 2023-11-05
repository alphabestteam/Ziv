const friendsArray = ["Sandy", "Patrick", "Squid", "Gary", "Pearl"];
console.log(friendsArray + ", Length: " + friendsArray.length);
friendsArray.push("Patchy");
console.log(friendsArray + ", Length: " + friendsArray.length);
friendsArray[0] = "Plankton";
console.log(friendsArray + ", Length: " + friendsArray.length);

/*
Declaring an array as const  means that the variable that points to the array cannot be changed to a different array.
However, the contents of the array can be changed( adding, deleting, and editing elements).
This is possible since the const keyword applies to the variable reference, and not the data in the array.
 */