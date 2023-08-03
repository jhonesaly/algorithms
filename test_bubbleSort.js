const assert = require('assert');
const bubbleSort = require('./bubbleSort');

describe('Bubble Sort', () => {
    it('should sort an range array in ascending order', () => {
        const testInput = [0, 1, 2, 3, 4, 5];
        const expectedOutput = [0, 1, 2, 3, 4, 5];
        assert.deepStrictEqual(bubbleSort(testInput), expectedOutput);
    });

    it('should sort a reverse range array in ascending order', () => {
        const testInput = testInput = [5, 4, 3, 2, 1, 0];
        const expectedOutput = [0, 1, 2, 3, 4, 5];
        assert.deepStrictEqual(bubbleSort(testInput), expectedOutput);
    });
});