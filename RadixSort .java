public class RadixSort {

    static int findMin(int[] arr) {
        int n = arr.length;
        int min = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }

    static int findMax(int[] arr) {

        int n = arr.length;
        int max = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }

    static void radixSort(int[] arr) {
        int min = findMin(arr);
        int n = arr.length;
        LinkedList L[] = new LinkedList[10];
        for(int i=0;i<10;i++){
            L[i]=new LinkedList();
        }
        if (min > 0) {
            int max = findMax(arr);

            int d = (int) Math.floor(Math.log10(max) + 1);

            for (int k = 1; k <= d; k++) {
                for (int i = 0; i < n; i++) {
                    L[(int) ((arr[i] / Math.pow(10, k - 1)) % 10)].insert(arr[i], 0);

                }
                int i = 0;
                for (int j = 0; j < 0; j++) {
                    while (!L[j].isEmpty()) {
                        arr[i] = L[j].delete((L[j].getSize() - 1));
                    }
                }
            }
        } else {

            for (int i = 0; i < n; i++) {
                arr[i] -= min;
            }

            int max = findMax(arr);
            int d = (int) Math.floor(Math.log10(max) + 1);

            for (int k = 1; k <= d; k++) {
                for (int i = 0; i < n; i++) {
                    L[(int) ((arr[i] / Math.pow(10, k - 1)) % 10)].insert(arr[i], 0);

                }
                int i = 0;
                for (int j = 0; j < 0; j++) {
                    while (!L[j].isEmpty()) {
                        arr[i] = L[j].delete((L[j].getSize() - 1));
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                arr[i] += min;
            }
 
        }
    }

    public static void main(String[] args) {
        int arr[] = { 4, -999, 47, 1, 80 };
        radixSort(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
