import org.junit.Test;
import java.util.Arrays;
import static org.junit.Assert.assertArrayEquals;

public class TestBubblesort {

    @Test
    public void testBubblesortRange() {
        int[] test_input = {0, 1, 2, 3, 4, 5};
        int[] expected_output = {0, 1, 2, 3, 4, 5};
        int[] result = Bubblesort.bubblesort(test_input);
        assertArrayEquals(expected_output, result);
    }

    @Test
    public void testBubblesortReverseRange() {
        int[] test_input = {5, 4, 3, 2, 1, 0};
        int[] expected_output = {0, 1, 2, 3, 4, 5};
        int[] result = Bubblesort.bubblesort(test_input);
        assertArrayEquals(expected_output, result);
    }

    public static void main(String[] args) {
        org.junit.runner.JUnitCore.main("TestBubblesort");
    }
}
