function bubbleSort(arr){
    let cont = true;

    while (cont) {
        let swapped = false;

        for (let i = 0; i < (arr.length - 1); i++) {
            if (arr[i] > arr[i+1]) {
                let temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                swapped = true;
            }
        
        if (swapped === false){
            cont = false;
        }
        }
    }
    return arr;
}

const array = bubbleSort([5,4,3,2,1,0]);
console.log(array);

module.exports = bubbleSort;