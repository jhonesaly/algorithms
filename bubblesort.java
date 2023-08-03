import java.util.Arrays;

public class bubblesort {

    public static int[] bubblesort(int[] arr) {
        boolean cont = true;

        while (cont) {
            boolean swapped = false;

            for (int i = 0; i < arr.length - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    swapped = true;
                    int a_1 = arr[i];
                    int a_2 = arr[i+1];
                    arr[i+1] = a_1;
                    arr[i] = a_2;
                }
            }

            if (!swapped) {
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