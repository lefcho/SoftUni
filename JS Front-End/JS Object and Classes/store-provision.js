function solve(currentStock, orderedStock) {
    let productStock = {}

    function organiseProducts(productArray, stock) {

        for(let i = 0; i < productArray.length; i++) {
            if (i % 2 == 0) {
                var currentProduct = productArray[i];
                if (!(currentProduct in stock)) {
                    stock[currentProduct] = 0;
                }
            } else {
                let quantityOfStock = Number(productArray[i]);
                stock[currentProduct] += quantityOfStock;
            }
        }
    }

    organiseProducts(currentStock, productStock);
    organiseProducts(orderedStock, productStock);
    for (const product in productStock) {
        console.log(`${product} -> ${productStock[product]}`);
    }
    
} 

solve(['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'],
    ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']);

console.log('----------------------------------');

solve([
    'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
    ],
    [
    'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
    ])

