// Daily Challenge: Car Inventory

// Part I
const inventory = [
  { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
  { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
  { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
  {
    id: 4,
    car_make: "Land Rover",
    car_model: "Defender Ice Edition",
    car_year: 2010,
  },
  { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];


function getCarHonda(blabla) {
  const hondaCar = blabla.find(function (car) {
    return car.car_make === "Honda";
  });

  if (hondaCar) {
    return `This is a ${hondaCar.car_make} ${hondaCar.car_model} from ${hondaCar.car_year}.`;
  } else {
    return "No Honda car found in the inventory.";
  }
}
console.log(getCarHonda(inventory));


function sortCarInventoryByYear(blabla) {
  const sortedBlabla = blabla.sort(function (car1, car2) {
    return car1.car_year - car2.car_year;
  });
  return sortedBlabla;
}
console.log(sortCarInventoryByYear(inventory));
