class Student {
    constructor(name, age, grades) {
      this.name = name;
      this.age = age;
      this.grades = grades;
    }
  
    calculateGradeAverage() {
        let gradeSum = 0;
        for (let grade of this.grades) {
            gradeSum += grade;
        }
        gradeSum /= this.grades.length; 
        gradeSum += (this.name.match(/[aeiouAEIOU]/g) || []).length;
        return gradeSum
      }
    }
  
const studentsArray = [
    new Student("Maya", 18, [85, 90, 78, 95, 88]),
    new Student("Coral", 16, [92, 75, 89, 94, 81]),
    new Student("Jordan", 19, [78, 86, 92, 80, 91]),
    new Student("Shahaf", 15, [89, 76, 85, 92, 87]),
    new Student("Ziv", 18, [80, 91, 88, 79, 93])
];

for (let index = 0; index < studentsArray.length; index++) {
    const student = studentsArray[index];
    console.log(`Student ${index}: Name: ${student.name}, Age: ${student.age}, Grades: ${student.grades}`);
}

const adults = studentsArray.filter(student => student.age >= 18);
console.log(adults)

class myCar {
    constructor(brand, model, productionYear) {
      this.brand = brand;
      this.model = model;
      this.productionYear = productionYear;
    }
    carAge() {
        const currentYear = new Date().getFullYear();
        return currentYear - this.productionYear;
    }
}

const carArray =[
    new myCar("Detroit", "Hudson Hornet", 1951),
    new myCar("Chevy Corvette", "C1", 1957),
    new myCar("Cadillac", "Coupe Deville", 1972)
]

for (let index = 0; index < carArray.length; index++) {
    const car = carArray[index];
    console.log(`Car ${index}: Brand: ${car.brand}, Model: ${car.model}, Production year: ${car.productionYear}`);
}