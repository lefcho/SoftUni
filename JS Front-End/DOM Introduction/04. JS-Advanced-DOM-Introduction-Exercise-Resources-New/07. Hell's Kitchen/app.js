function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      const textAreaElement = document.querySelector('#inputs > textarea')
      const restaurantsArray = JSON.parse(textAreaElement.value);
      const bestRestaurantElement = document.querySelector('#bestRestaurant > p');
      const bestWorkersElement = document.querySelector('#workers > p')
      const restaurants = {};
      

      for (const restaurantInfo of restaurantsArray) {

         let [restaurantName, workersInfo] = restaurantInfo.split(' - ');
         if (!restaurants[restaurantName]) {
            const organisedInfo = {};
            workersInfo
               .split(', ')
               .map(workerInfo => {
                  let [name, salary] = workerInfo.split(' ');
                  organisedInfo[name] = Number(salary);
               });
            restaurants[restaurantName] = organisedInfo;
         } else {
            workersInfo
               .split(', ')
               .map(workerInfo => {
                  let [name, salary] = workerInfo.split(' ');
                  restaurants[restaurantName][name] = salary;
            });
         }
      }

      let bestAvgSalary = Number.MIN_SAFE_INTEGER;
      let bestSalary = Number.MIN_SAFE_INTEGER;
      let bestRestaurant = '';
      let bestSalaries = '';

      for (const restaurant in restaurants) {
         let restaurantValues = Object.values(restaurants[restaurant])
         let avgSalary = restaurantValues.reduce((a, b) => a + b, 0) / restaurantValues.length;
         if (avgSalary > bestAvgSalary) {
            bestAvgSalary = avgSalary;
            bestSalary = restaurantValues.reduce((a, b) => Math.max(a, b), -Infinity);
            bestRestaurant = restaurant;
         }
      }

      const entries = Object.entries(restaurants[bestRestaurant]);
      entries.sort((a, b) => b[1] - a[1]);

      for (const worker of entries) {
         bestSalaries += `Name: ${worker[0]} With Salary: ${worker[1]} `;
      }

      bestRestaurantElement.textContent = `Name: ${bestRestaurant} Average Salary: ${bestAvgSalary.toFixed(2)} Best Salary: ${bestSalary.toFixed(2)}`
      bestWorkersElement.textContent = bestSalaries;
}
}