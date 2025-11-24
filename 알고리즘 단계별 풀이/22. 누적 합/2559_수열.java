import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        int[] array = new int[N];
        for(int i = 0; i < N; i++) {
            array[i] = scanner.nextInt();
        }

        int max_sum = 0;
        for(int i = 0; i < K; i++) {
            max_sum += array[i];
        }

        int temp_sum = max_sum;
        for(int i = 1; i < N - K + 1; i++) {
            temp_sum = temp_sum - array[i - 1] + array[i + K - 1];
            if(max_sum < temp_sum) {
                max_sum = temp_sum;
            }
        }
        System.out.println(max_sum);
        scanner.close();
    }
}