import java.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;
import java.io.PrintStream;

class RadixSort {
    public static void main(String[] args) {
      try {
      int[] arr = readData1("C:/Users/tnish/OneDrive/Desktop/test.txt");
      PrintStream myconsole = new PrintStream(new File("C:/Users/tnish/OneDrive/Desktop/", "test1234.txt"));
      System.setOut(myconsole);
      radixSort(arr);
      myconsole.println(Arrays.toString(arr));
        
      } catch (Exception e) {
        System.out.println(e);
      }
    }
      
    private static void radixSort(int[] arr){
      //get max element in array
      int max = getMaxElementInArray(arr);
      int position = 1;
      // move from least significant digit 
      // to most significant digit
      while(max/position > 0){
        countingSort(arr, position);
        position *= 10;
      }        
    }
      
    private static int getMaxElementInArray(int[] arr){
      int max = arr[0];
      for(int i = 1; i < arr.length; i++){
        if (arr[i] > max){
            max = arr[i];
        }
      }
      return max;
    }
      
    // Counting sort used to sort array in each pass
    private static void countingSort(int[] arr, int position){
      int n = arr.length;
      int[] output = new int[n];
      int[] count = new int[n];
          
      //Calculate frequency of each element, put it in count array
      for(int i = 0; i < arr.length; i++){
        count[(arr[i]/position)%10]++;
      }
      // Modify count array to get the final position of elements
      for(int i = 1; i < n; i++){
        count[i] = count[i] + count[i-1];
      }
      
      // Add elements to output array for this pass
      for(int i = n-1; i >=0; i--){
        output[count[(arr[i]/position)%10] - 1] = arr[i];
        count[(arr[i]/position)%10]--;
      }
      for(int i = 0; i < output.length; i++){
        arr[i] = output[i];
      }
      System.out.println(Arrays.toString(arr));
                 
    }

    public static int[] readData1(String file_location){
      String line = null;
      String [] array = new String[10];
      int [] array_int = new int[10];
      try {
        BufferedReader br = new BufferedReader(new FileReader(file_location));  
        while ((line = br.readLine()) != null) {
          array = line.split(",");
        }
        for (int i = 0; i < array.length; i++) {
          array_int[i] = Integer.valueOf(array[i]);
        }
        br.close();
      } catch (Exception e) {
        System.out.print(e);
      }
      return array_int;
    }
  }

