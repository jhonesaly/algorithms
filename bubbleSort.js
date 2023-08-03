function bubbleSort(arr) {
    let cont = true;

    while (cont === true) {
        let swapped = false;

        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                swapped = true;
                let temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }

        if (swapped === false) {
            cont = false;
        }
    }

    return arr;
}

module.exports = bubbleSort;