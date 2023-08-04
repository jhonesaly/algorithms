import java.util.Arrays;

public class bubblesort {
    
    public static int[] bubblesort(int[] arr) {
        boolean cont = true;
        while (cont) {
            boolean swapped = false;

            for (int i = 0; i < arr.length - 1; i++) {
                if (arr[i] > arr[i+1]) {
                    int temp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = temp;
                    swapped = true;
                }
            }

            if (swapped == false) {
                cont = false;
            }
        }

        return arr;
    }


    public static void main(String[] args) {
        int[] test_input = {5, 4, 3, 2, 1, 0};
        int[] result = bubblesort(test_input);

        System.out.println(Arrays.toString(result));
    }
}