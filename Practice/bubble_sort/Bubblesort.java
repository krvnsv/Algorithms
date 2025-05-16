package bubblesort;
import java.util.Arrays;

public class Bubblesort {

    public static void main(String[] args) {

        Sort s = new Sort();
        int arr[] = {11, 1, 2, 12, 3, 13, 4, 14, 5, 15};
        System.out.println("Original array " + Arrays.toString(arr));
        s.bubbleSort(arr);
        System.out.println("Sorted array " + Arrays.toString(arr));
    }
}